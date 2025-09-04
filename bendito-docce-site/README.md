# Site Bendito Docce - Documentação Completa

## 📋 Visão Geral

Este é um site responsivo completo para a doceria **Bendito Docce**, desenvolvido com HTML, CSS e JavaScript puros. O site inclui funcionalidades avançadas como carrinho de compras, área administrativa para gerenciar produtos e seção especial para novidades.

## 🚀 Funcionalidades Principais

### ✅ Carrinho de Compras Completo
- **Adicionar produtos** com quantidade personalizada
- **Visualizar carrinho lateral** com produtos adicionados
- **Alterar quantidades** diretamente no carrinho
- **Remover produtos** individualmente
- **Cálculo automático** de preços (unitário vs. cento)
- **Finalização via WhatsApp** com mensagem formatada
- **Persistência** dos dados no localStorage

### ✅ Catálogo de Produtos
- **Grid responsivo** com produtos organizados
- **Imagens de alta qualidade** dos brigadeiros
- **Preços diferenciados** (unitário e por cento)
- **Seletor de quantidade** intuitivo
- **Botões de ação rápida** (hover effects)

### ✅ Seção de Novidades
- **Área dedicada** para novos produtos
- **Badge "Novo!"** para destacar lançamentos
- **Layout diferenciado** com bordas especiais
- **Fácil identificação** visual

### ✅ Painel Administrativo
- **Adicionar novos produtos** via formulário
- **Gerenciar produtos existentes**
- **Categorização** (tradicional, gourmet, novo)
- **Upload de imagens** via URL
- **Exclusão de produtos** com confirmação

### ✅ Design Responsivo
- **Mobile-first** approach
- **Menu hamburger** para dispositivos móveis
- **Grid adaptativo** para diferentes telas
- **Imagens otimizadas** para carregamento rápido

### ✅ Experiência do Usuário
- **Animações suaves** e transições
- **Notificações** de ações realizadas
- **Navegação intuitiva** com scroll suave
- **Botão voltar ao topo**
- **Loading states** e feedback visual

## 📁 Estrutura de Arquivos

```
bendito-docce-site/
├── index.html          # Página principal
├── style.css           # Estilos e responsividade
├── script.js           # Funcionalidades JavaScript
├── logo.jpeg           # Logo da empresa
├── img1.jpeg           # Imagem dos produtos 1
├── img2.jpeg           # Imagem dos produtos 2
├── img3.jpeg           # Imagem dos produtos 3
└── README.md           # Esta documentação
```

## 🎨 Paleta de Cores

- **Primária**: `#8B4B6B` (Rosa escuro)
- **Secundária**: `#F7D6DC` (Rosa claro)
- **Accent**: `#E69CB3` (Rosa médio)
- **Texto**: `#5C4033` (Marrom)
- **Background**: `#FFFAFC` (Branco rosado)

## 📱 Seções do Site

### 1. Header
- Logo da empresa
- Título e slogan
- Ícone do carrinho com contador

### 2. Navegação
- Menu responsivo
- Links para todas as seções
- Acesso ao painel admin

### 3. Hero Section
- Apresentação principal
- Call-to-action
- Imagem destacada

### 4. Produtos
- Grid de produtos tradicionais e gourmet
- Seletor de quantidade
- Botões de adicionar ao carrinho

### 5. Novidades
- Produtos marcados como "novo"
- Layout especial com destaque

### 6. Galeria
- Showcase das criações
- Efeitos hover
- Imagens em alta qualidade

### 7. Contato
- Informações de contato
- Mapa integrado
- Links para redes sociais

### 8. Admin (Oculto)
- Formulário para novos produtos
- Lista de produtos cadastrados
- Opções de edição e exclusão

### 9. Footer
- Informações da empresa
- Horário de funcionamento
- Copyright

## 🛠️ Como Usar o Painel Admin

### Acessar o Painel
1. Clique no link "Admin" no menu de navegação
2. O painel será exibido na parte inferior da página

### Adicionar Novo Produto
1. Preencha o formulário com:
   - **Nome do Produto**: Nome descritivo
   - **Preço**: Valor unitário em reais
   - **Descrição**: Breve descrição do sabor
   - **URL da Imagem**: Link para imagem do produto
   - **Categoria**: Selecione entre tradicional, gourmet ou novo

2. Clique em "Adicionar Produto"
3. O produto aparecerá automaticamente na seção correspondente

### Gerenciar Produtos Existentes
- Visualize todos os produtos na lista do admin
- Use o botão de lixeira para excluir produtos
- Confirmação será solicitada antes da exclusão

## 🛒 Como Funciona o Carrinho

### Adicionar Produtos
1. **Selecione a quantidade** usando os botões + e -
2. **Clique em "Adicionar ao Carrinho"**
3. **Receba confirmação visual** da ação

### Visualizar Carrinho
1. **Clique no ícone do carrinho** no header
2. **Veja todos os produtos** adicionados
3. **Altere quantidades** diretamente no carrinho

### Finalizar Pedido
1. **Revise os itens** no carrinho
2. **Clique em "Finalizar Pedido"**
3. **Será redirecionado para WhatsApp** com mensagem formatada

## 💰 Sistema de Preços

O site implementa um sistema inteligente de preços:

- **Menos de 100 unidades**: Preço unitário
- **100 ou mais unidades**: Preço especial por cento (desconto automático)

Exemplo:
- Brigadeiro Ferrero Rocher: R$ 4,50 unitário ou R$ 150,00 o cento
- Economia de R$ 300,00 ao comprar 100 unidades!

## 📱 Responsividade

### Desktop (1200px+)
- Layout em grid de 3 colunas
- Carrinho lateral de 400px
- Menu horizontal completo

### Tablet (768px - 1199px)
- Grid adaptativo de 2 colunas
- Carrinho ocupa largura total
- Menu ainda horizontal

### Mobile (até 767px)
- Grid de 1 coluna
- Menu hamburger
- Carrinho em tela cheia
- Botões maiores para touch

## 🔧 Personalização

### Alterar Cores
Edite as variáveis CSS no início do arquivo `style.css`:

```css
:root {
    --primary-color: #8B4B6B;
    --secondary-color: #F7D6DC;
    --accent-color: #E69CB3;
    /* ... outras cores */
}
```

### Adicionar Novos Produtos via Código
Edite o array `products` no arquivo `script.js`:

```javascript
products.push({
    id: 7,
    name: "Novo Sabor",
    price: 4.00,
    pricePerHundred: 140.00,
    description: "Descrição do sabor",
    image: "nova-imagem.jpeg",
    category: "novo"
});
```

### Personalizar Mensagem do WhatsApp
Edite a função `checkout()` no arquivo `script.js` para alterar o formato da mensagem.

## 🚀 Deploy e Hospedagem

### Opção 1: Servidor Local
```bash
# Navegue até a pasta do projeto
cd bendito-docce-site

# Inicie um servidor HTTP simples
python3 -m http.server 8000

# Acesse http://localhost:8000
```

### Opção 2: Hospedagem Web
1. **Faça upload** de todos os arquivos para seu servidor
2. **Configure o domínio** para apontar para a pasta
3. **Teste todas as funcionalidades**

### Opção 3: GitHub Pages
1. **Crie um repositório** no GitHub
2. **Faça upload** dos arquivos
3. **Ative GitHub Pages** nas configurações
4. **Acesse via URL** fornecida pelo GitHub

## 🔒 Segurança e Boas Práticas

### Dados do Carrinho
- Armazenados localmente no navegador
- Não enviados para servidores externos
- Limpos automaticamente após finalização

### Formulário Admin
- Validação client-side
- Sanitização básica de inputs
- Confirmação para ações destrutivas

### Imagens
- Carregamento otimizado
- Fallback para imagens quebradas
- Compressão recomendada

## 🐛 Solução de Problemas

### Carrinho não funciona
- Verifique se JavaScript está habilitado
- Limpe o localStorage do navegador
- Recarregue a página

### Imagens não carregam
- Verifique se os arquivos estão na pasta correta
- Confirme os nomes dos arquivos
- Teste com URLs absolutas

### Layout quebrado no mobile
- Verifique a meta tag viewport
- Teste em diferentes dispositivos
- Use ferramentas de desenvolvedor

### WhatsApp não abre
- Verifique se o número está correto
- Teste em dispositivo com WhatsApp instalado
- Confirme a formatação da mensagem

## 📞 Suporte

Para dúvidas ou problemas:

1. **Verifique esta documentação** primeiro
2. **Teste em navegador atualizado**
3. **Consulte o console** do navegador para erros
4. **Entre em contato** com o desenvolvedor

## 🔄 Atualizações Futuras

### Funcionalidades Planejadas
- [ ] Sistema de login para admin
- [ ] Banco de dados para produtos
- [ ] Integração com pagamento online
- [ ] Sistema de avaliações
- [ ] Newsletter e promoções
- [ ] Programa de fidelidade

### Melhorias Técnicas
- [ ] Service Worker para cache
- [ ] Otimização de imagens automática
- [ ] Testes automatizados
- [ ] Monitoramento de performance
- [ ] SEO avançado

---

**Desenvolvido com ❤️ para Bendito Docce**

*Última atualização: Janeiro 2025*

