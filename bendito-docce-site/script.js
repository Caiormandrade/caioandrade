// Dados dos produtos
let products = [
    {
        id: 1,
        name: "Brigadeiro Ferrero Rocher",
        price: 4.50,
        pricePerHundred: 150.00,
        description: "Brigadeiro gourmet com sabor Ferrero Rocher",
        image: "img1.jpeg",
        category: "gourmet"
    },
    {
        id: 2,
        name: "Brigadeiro Red Velvet",
        price: 4.00,
        pricePerHundred: 150.00,
        description: "Brigadeiro com sabor Red Velvet",
        image: "img2.jpeg",
        category: "gourmet"
    },
    {
        id: 3,
        name: "Brigadeiro Churros",
        price: 3.50,
        pricePerHundred: 150.00,
        description: "Brigadeiro com sabor de churros",
        image: "img1.jpeg",
        category: "gourmet"
    },
    {
        id: 4,
        name: "Brigadeiro Maracujá",
        price: 3.50,
        pricePerHundred: 150.00,
        description: "Brigadeiro com sabor de maracujá",
        image: "img2.jpeg",
        category: "gourmet"
    },
    {
        id: 5,
        name: "Brigadeiro Tradicional",
        price: 3.00,
        pricePerHundred: 130.00,
        description: "Brigadeiro tradicional de chocolate",
        image: "img1.jpeg",
        category: "tradicional"
    },
    {
        id: 6,
        name: "Brigadeiro Ninho com Nutella",
        price: 5.00,
        pricePerHundred: 180.00,
        description: "Brigadeiro de leite ninho com nutella",
        image: "img2.jpeg",
        category: "novo"
    }
];

// Carrinho de compras
let cart = [];
let cartCount = 0;
let cartTotal = 0;

// Inicialização
document.addEventListener('DOMContentLoaded', function() {
    loadProducts();
    loadNewProducts();
    setupEventListeners();
    loadCartFromStorage();
    updateCartDisplay();
});

// Configurar event listeners
function setupEventListeners() {
    // Navegação suave
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            
            if (targetId === 'admin') {
                toggleAdminSection();
                return;
            }
            
            const targetSection = document.getElementById(targetId);
            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Menu hamburger
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    
    hamburger.addEventListener('click', function() {
        hamburger.classList.toggle('active');
        navMenu.classList.toggle('active');
    });

    // Botão voltar ao topo
    const backToTopBtn = document.getElementById('backToTop');
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            backToTopBtn.style.display = 'block';
        } else {
            backToTopBtn.style.display = 'none';
        }
    });

    backToTopBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // Form de adicionar produto
    const addProductForm = document.getElementById('addProductForm');
    addProductForm.addEventListener('submit', function(e) {
        e.preventDefault();
        addNewProduct();
    });
}

// Carregar produtos na seção principal
function loadProducts() {
    const productsGrid = document.getElementById('productsGrid');
    const regularProducts = products.filter(p => p.category !== 'novo');
    
    productsGrid.innerHTML = regularProducts.map(product => `
        <div class="product-card">
            <div class="product-image">
                <img src="${product.image}" alt="${product.name}">
                <div class="product-overlay">
                    <button class="quick-add-btn" onclick="addToCart(${product.id}, 1)">
                        <i class="fas fa-plus"></i>
                    </button>
                </div>
            </div>
            <div class="product-info">
                <h3>${product.name}</h3>
                <p class="product-description">${product.description}</p>
                <div class="product-prices">
                    <span class="unit-price">Unidade: R$ ${product.price.toFixed(2)}</span>
                    <span class="hundred-price">Cento: R$ ${product.pricePerHundred.toFixed(2)}</span>
                </div>
                <div class="product-actions">
                    <div class="quantity-selector">
                        <button onclick="changeQuantity(${product.id}, -1)">-</button>
                        <input type="number" id="qty-${product.id}" value="1" min="1" max="100">
                        <button onclick="changeQuantity(${product.id}, 1)">+</button>
                    </div>
                    <button class="add-to-cart-btn" onclick="addToCartWithQuantity(${product.id})">
                        Adicionar ao Carrinho
                    </button>
                </div>
            </div>
        </div>
    `).join('');
}

// Carregar novos produtos
function loadNewProducts() {
    const newProductsGrid = document.getElementById('newProductsGrid');
    const newProducts = products.filter(p => p.category === 'novo');
    
    if (newProducts.length === 0) {
        newProductsGrid.innerHTML = '<p class="no-products">Nenhuma novidade no momento. Volte em breve!</p>';
        return;
    }
    
    newProductsGrid.innerHTML = newProducts.map(product => `
        <div class="product-card new-product">
            <div class="new-badge">Novo!</div>
            <div class="product-image">
                <img src="${product.image}" alt="${product.name}">
                <div class="product-overlay">
                    <button class="quick-add-btn" onclick="addToCart(${product.id}, 1)">
                        <i class="fas fa-plus"></i>
                    </button>
                </div>
            </div>
            <div class="product-info">
                <h3>${product.name}</h3>
                <p class="product-description">${product.description}</p>
                <div class="product-prices">
                    <span class="unit-price">Unidade: R$ ${product.price.toFixed(2)}</span>
                    <span class="hundred-price">Cento: R$ ${product.pricePerHundred.toFixed(2)}</span>
                </div>
                <div class="product-actions">
                    <div class="quantity-selector">
                        <button onclick="changeQuantity(${product.id}, -1)">-</button>
                        <input type="number" id="qty-${product.id}" value="1" min="1" max="100">
                        <button onclick="changeQuantity(${product.id}, 1)">+</button>
                    </div>
                    <button class="add-to-cart-btn" onclick="addToCartWithQuantity(${product.id})">
                        Adicionar ao Carrinho
                    </button>
                </div>
            </div>
        </div>
    `).join('');
}

// Alterar quantidade
function changeQuantity(productId, change) {
    const qtyInput = document.getElementById(`qty-${productId}`);
    let currentQty = parseInt(qtyInput.value);
    let newQty = currentQty + change;
    
    if (newQty < 1) newQty = 1;
    if (newQty > 100) newQty = 100;
    
    qtyInput.value = newQty;
}

// Adicionar ao carrinho com quantidade
function addToCartWithQuantity(productId) {
    const qtyInput = document.getElementById(`qty-${productId}`);
    const quantity = parseInt(qtyInput.value);
    addToCart(productId, quantity);
}

// Adicionar produto ao carrinho
function addToCart(productId, quantity = 1) {
    const product = products.find(p => p.id === productId);
    if (!product) return;

    const existingItem = cart.find(item => item.id === productId);
    
    if (existingItem) {
        existingItem.quantity += quantity;
    } else {
        cart.push({
            id: product.id,
            name: product.name,
            price: product.price,
            pricePerHundred: product.pricePerHundred,
            quantity: quantity,
            image: product.image
        });
    }
    
    updateCartDisplay();
    saveCartToStorage();
    showAddToCartNotification(product.name, quantity);
}

// Remover do carrinho
function removeFromCart(productId) {
    cart = cart.filter(item => item.id !== productId);
    updateCartDisplay();
    saveCartToStorage();
}

// Atualizar quantidade no carrinho
function updateCartQuantity(productId, newQuantity) {
    if (newQuantity <= 0) {
        removeFromCart(productId);
        return;
    }
    
    const item = cart.find(item => item.id === productId);
    if (item) {
        item.quantity = newQuantity;
        updateCartDisplay();
        saveCartToStorage();
    }
}

// Atualizar exibição do carrinho
function updateCartDisplay() {
    const cartItems = document.getElementById('cartItems');
    const cartCountElement = document.querySelector('.cart-count');
    const cartTotalElement = document.getElementById('cartTotal');
    
    cartCount = cart.reduce((total, item) => total + item.quantity, 0);
    cartTotal = cart.reduce((total, item) => {
        const price = item.quantity >= 100 ? item.pricePerHundred / 100 : item.price;
        return total + (price * item.quantity);
    }, 0);
    
    cartCountElement.textContent = cartCount;
    cartTotalElement.textContent = cartTotal.toFixed(2);
    
    if (cart.length === 0) {
        cartItems.innerHTML = '<p class="empty-cart">Seu carrinho está vazio</p>';
    } else {
        cartItems.innerHTML = cart.map(item => {
            const price = item.quantity >= 100 ? item.pricePerHundred / 100 : item.price;
            const subtotal = price * item.quantity;
            
            return `
                <div class="cart-item">
                    <img src="${item.image}" alt="${item.name}">
                    <div class="cart-item-info">
                        <h4>${item.name}</h4>
                        <p class="cart-item-price">R$ ${price.toFixed(2)} cada</p>
                        <div class="cart-item-controls">
                            <button onclick="updateCartQuantity(${item.id}, ${item.quantity - 1})">-</button>
                            <span>${item.quantity}</span>
                            <button onclick="updateCartQuantity(${item.id}, ${item.quantity + 1})">+</button>
                        </div>
                    </div>
                    <div class="cart-item-total">
                        <p>R$ ${subtotal.toFixed(2)}</p>
                        <button class="remove-item" onclick="removeFromCart(${item.id})">
                            <i class="fas fa-trash"></i>
                        </button>
                    </div>
                </div>
            `;
        }).join('');
    }
}

// Toggle carrinho
function toggleCart() {
    const cartSidebar = document.getElementById('cartSidebar');
    const cartOverlay = document.getElementById('cartOverlay');
    
    cartSidebar.classList.toggle('active');
    cartOverlay.classList.toggle('active');
    document.body.classList.toggle('cart-open');
}

// Finalizar pedido
function checkout() {
    if (cart.length === 0) {
        alert('Seu carrinho está vazio!');
        return;
    }
    
    let message = 'Olá! Gostaria de fazer o seguinte pedido:\n\n';
    
    cart.forEach(item => {
        const price = item.quantity >= 100 ? item.pricePerHundred / 100 : item.price;
        const subtotal = price * item.quantity;
        message += `• ${item.name} - Quantidade: ${item.quantity} - Subtotal: R$ ${subtotal.toFixed(2)}\n`;
    });
    
    message += `\nTotal: R$ ${cartTotal.toFixed(2)}`;
    
    const whatsappUrl = `https://wa.me/5535984089245?text=${encodeURIComponent(message)}`;
    window.open(whatsappUrl, '_blank');
}

// Salvar carrinho no localStorage
function saveCartToStorage() {
    localStorage.setItem('benditoDocceCart', JSON.stringify(cart));
}

// Carregar carrinho do localStorage
function loadCartFromStorage() {
    const savedCart = localStorage.getItem('benditoDocceCart');
    if (savedCart) {
        cart = JSON.parse(savedCart);
    }
}

// Notificação de produto adicionado
function showAddToCartNotification(productName, quantity) {
    const notification = document.createElement('div');
    notification.className = 'add-to-cart-notification';
    notification.innerHTML = `
        <i class="fas fa-check-circle"></i>
        <span>${quantity}x ${productName} adicionado ao carrinho!</span>
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.classList.add('show');
    }, 100);
    
    setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// Seção Admin
function toggleAdminSection() {
    const adminSection = document.getElementById('admin');
    const isVisible = adminSection.style.display !== 'none';
    
    if (isVisible) {
        adminSection.style.display = 'none';
    } else {
        adminSection.style.display = 'block';
        adminSection.scrollIntoView({ behavior: 'smooth' });
        loadAdminProducts();
    }
}

// Adicionar novo produto
function addNewProduct() {
    const name = document.getElementById('productName').value;
    const price = parseFloat(document.getElementById('productPrice').value);
    const description = document.getElementById('productDescription').value;
    const image = document.getElementById('productImage').value || 'img1.jpeg';
    const category = document.getElementById('productCategory').value;
    
    const newProduct = {
        id: products.length + 1,
        name: name,
        price: price,
        pricePerHundred: price * 100 * 0.85, // Desconto para cento
        description: description,
        image: image,
        category: category
    };
    
    products.push(newProduct);
    
    // Recarregar produtos
    loadProducts();
    loadNewProducts();
    loadAdminProducts();
    
    // Limpar formulário
    document.getElementById('addProductForm').reset();
    
    alert('Produto adicionado com sucesso!');
}

// Carregar produtos no admin
function loadAdminProducts() {
    const adminProductsList = document.getElementById('adminProductsList');
    
    adminProductsList.innerHTML = products.map(product => `
        <div class="admin-product-item">
            <img src="${product.image}" alt="${product.name}">
            <div class="admin-product-info">
                <h4>${product.name}</h4>
                <p>Preço: R$ ${product.price.toFixed(2)}</p>
                <p>Categoria: ${product.category}</p>
            </div>
            <button class="admin-delete-btn" onclick="deleteProduct(${product.id})">
                <i class="fas fa-trash"></i>
            </button>
        </div>
    `).join('');
}

// Deletar produto
function deleteProduct(productId) {
    if (confirm('Tem certeza que deseja deletar este produto?')) {
        products = products.filter(p => p.id !== productId);
        loadProducts();
        loadNewProducts();
        loadAdminProducts();
    }
}

// Animações de scroll
function handleScrollAnimations() {
    const elements = document.querySelectorAll('.product-card, .gallery-item, .contact-item');
    
    elements.forEach(element => {
        const elementTop = element.getBoundingClientRect().top;
        const elementVisible = 150;
        
        if (elementTop < window.innerHeight - elementVisible) {
            element.classList.add('animate');
        }
    });
}

window.addEventListener('scroll', handleScrollAnimations);

// Notificação de boas-vindas
window.addEventListener('load', function() {
    setTimeout(() => {
        const welcome = document.createElement('div');
        welcome.className = 'welcome-notification';
        welcome.innerHTML = `
            <i class="fas fa-heart"></i>
            <span>Bem-vindo(a) à Bendito Docce! 🍫</span>
        `;
        
        document.body.appendChild(welcome);
        
        setTimeout(() => {
            welcome.classList.add('show');
        }, 500);
        
        setTimeout(() => {
            welcome.classList.remove('show');
            setTimeout(() => {
                if (document.body.contains(welcome)) {
                    document.body.removeChild(welcome);
                }
            }, 300);
        }, 4000);
    }, 1000);
});

