# Manual do Administrador - Bendito Docce

## 🔐 Acesso ao Painel Administrativo

### Como Acessar
1. **Abra o site** da Bendito Docce
2. **Clique em "Admin"** no menu de navegação
3. **Role até o final** da página para ver o painel

> **Nota**: O painel admin é oculto por padrão para visitantes normais, mas sempre acessível via menu.

## ➕ Adicionando Novos Produtos

### Passo a Passo Completo

#### 1. Preparar Informações do Produto
Antes de adicionar, tenha em mãos:
- **Nome do produto** (ex: "Brigadeiro Morango")
- **Preço unitário** (ex: 4.50)
- **Descrição** (ex: "Brigadeiro com sabor de morango")
- **Imagem do produto** (foto ou URL)
- **Categoria** (tradicional, gourmet ou novo)

#### 2. Preencher o Formulário
1. **Nome do Produto**
   - Digite o nome completo
   - Use nomes descritivos e atrativos
   - Exemplo: "Brigadeiro Cookies & Cream"

2. **Preço (R$)**
   - Digite apenas o valor numérico
   - Use ponto para decimais (ex: 4.50)
   - O sistema calculará automaticamente o preço por cento

3. **Descrição**
   - Escreva uma descrição atrativa
   - Mencione ingredientes especiais
   - Máximo de 2-3 linhas

4. **URL da Imagem**
   - Cole o link completo da imagem
   - Ou use uma das imagens existentes: `img1.jpeg`, `img2.jpeg`, `img3.jpeg`
   - Certifique-se que a imagem seja de boa qualidade

5. **Categoria**
   - **Tradicional**: Sabores clássicos (chocolate, coco, etc.)
   - **Gourmet**: Sabores sofisticados (Ferrero Rocher, Red Velvet, etc.)
   - **Novo**: Lançamentos e novidades

#### 3. Confirmar Adição
1. **Clique em "Adicionar Produto"**
2. **Aguarde a confirmação** "Produto adicionado com sucesso!"
3. **Verifique** se o produto apareceu na seção correspondente

### Exemplos de Produtos

#### Produto Tradicional
```
Nome: Brigadeiro de Coco
Preço: 3.00
Descrição: Brigadeiro tradicional coberto com coco ralado
URL da Imagem: img1.jpeg
Categoria: tradicional
```

#### Produto Gourmet
```
Nome: Brigadeiro Pistache
Preço: 5.50
Descrição: Brigadeiro gourmet com pistache importado
URL da Imagem: img2.jpeg
Categoria: gourmet
```

#### Produto Novo
```
Nome: Brigadeiro Açaí
Preço: 4.80
Descrição: Novidade! Brigadeiro com sabor de açaí
URL da Imagem: img3.jpeg
Categoria: novo
```

## 🗂️ Gerenciando Produtos Existentes

### Visualizar Produtos
- **Lista completa** aparece no painel admin
- **Informações mostradas**: Nome, preço, categoria
- **Imagem miniatura** para identificação rápida

### Excluir Produtos
1. **Localize o produto** na lista
2. **Clique no ícone da lixeira** (🗑️)
3. **Confirme a exclusão** na janela que aparecer
4. **Produto será removido** imediatamente

> **⚠️ Atenção**: A exclusão é permanente e não pode ser desfeita!

## 💰 Sistema de Preços Automático

### Como Funciona
O sistema calcula automaticamente:
- **Preço unitário**: Valor que você define
- **Preço por cento**: Calculado com 15% de desconto

### Exemplo de Cálculo
```
Preço unitário: R$ 4,00
Preço por 100 unidades: R$ 4,00 × 100 × 0,85 = R$ 340,00
Economia para o cliente: R$ 60,00
```

### Ajustar Fórmula de Desconto
Para alterar a porcentagem de desconto, edite no arquivo `script.js`:

```javascript
// Linha aproximada 45
pricePerHundred: price * 100 * 0.85, // 0.85 = 15% desconto
```

Altere `0.85` para:
- `0.80` = 20% desconto
- `0.90` = 10% desconto
- `0.75` = 25% desconto

## 📸 Gerenciamento de Imagens

### Opções para Imagens

#### Opção 1: Usar Imagens Existentes
- `img1.jpeg` - Brigadeiros em caixinha
- `img2.jpeg` - Brigadeiros variados
- `img3.jpeg` - Cardápio visual
- `logo.jpeg` - Logo da empresa

#### Opção 2: Upload de Novas Imagens
1. **Faça upload** da imagem para o servidor
2. **Anote o caminho** completo
3. **Use o caminho** no campo URL da Imagem

#### Opção 3: Usar URLs Externas
1. **Hospede a imagem** em serviço como Imgur, Google Drive, etc.
2. **Copie o link direto** da imagem
3. **Cole no campo** URL da Imagem

### Dicas para Boas Imagens
- **Resolução**: Mínimo 300x300 pixels
- **Formato**: JPG ou PNG
- **Qualidade**: Alta definição
- **Iluminação**: Bem iluminada
- **Foco**: Produto em destaque

## 🎯 Estratégias de Categorização

### Categoria "Tradicional"
**Use para:**
- Sabores clássicos
- Produtos básicos
- Preços mais acessíveis
- Brigadeiros simples

**Exemplos:**
- Brigadeiro tradicional
- Brigadeiro de coco
- Brigadeiro de amendoim
- Bicho de pé

### Categoria "Gourmet"
**Use para:**
- Sabores sofisticados
- Ingredientes premium
- Preços mais altos
- Produtos elaborados

**Exemplos:**
- Ferrero Rocher
- Red Velvet
- Churros
- Maracujá
- Pistache

### Categoria "Novo"
**Use para:**
- Lançamentos recentes
- Sabores experimentais
- Produtos sazonais
- Edições limitadas

**Exemplos:**
- Sabores de época (Páscoa, Natal)
- Novos sabores em teste
- Colaborações especiais
- Tendências do mercado

## 📊 Monitoramento e Análise

### Acompanhar Performance
**Observe:**
- Quais produtos são mais adicionados ao carrinho
- Feedback dos clientes via WhatsApp
- Produtos que não vendem bem

### Otimizar Catálogo
**Ações recomendadas:**
- **Remover** produtos com baixa procura
- **Destacar** produtos populares como "novo"
- **Ajustar preços** conforme demanda
- **Adicionar** variações de produtos populares

## 🔄 Rotina de Manutenção

### Diária
- [ ] Verificar se todos os produtos estão visíveis
- [ ] Testar funcionamento do carrinho
- [ ] Responder mensagens do WhatsApp

### Semanal
- [ ] Revisar produtos na categoria "novo"
- [ ] Atualizar imagens se necessário
- [ ] Verificar preços da concorrência

### Mensal
- [ ] Analisar produtos mais vendidos
- [ ] Planejar novos lançamentos
- [ ] Fazer backup dos dados
- [ ] Otimizar descrições dos produtos

## 🚨 Solução de Problemas Comuns

### Produto não aparece após adicionar
**Possíveis causas:**
- Erro no preenchimento do formulário
- JavaScript desabilitado
- Cache do navegador

**Soluções:**
1. Recarregue a página (F5)
2. Verifique se todos os campos foram preenchidos
3. Tente novamente com dados diferentes

### Imagem não carrega
**Possíveis causas:**
- URL incorreta
- Imagem muito grande
- Servidor da imagem fora do ar

**Soluções:**
1. Verifique se a URL está correta
2. Teste a URL em nova aba do navegador
3. Use uma das imagens padrão temporariamente

### Preço calculado errado
**Possíveis causas:**
- Uso de vírgula em vez de ponto
- Caracteres especiais no preço

**Soluções:**
1. Use apenas números e ponto decimal
2. Exemplo correto: 4.50
3. Exemplo incorreto: 4,50 ou R$ 4,50

## 📱 Acesso Mobile

### Usar Admin no Celular
1. **Abra o site** no navegador do celular
2. **Toque em "Admin"** no menu
3. **Role até o formulário**
4. **Preencha normalmente**

### Dicas para Mobile
- **Use teclado numérico** para preços
- **Copie e cole** URLs de imagem
- **Teste o produto** após adicionar
- **Verifique a visualização** em diferentes telas

## 🎓 Dicas Avançadas

### Nomear Produtos Estrategicamente
- **Use palavras-chave** que clientes procuram
- **Seja específico** sobre sabores
- **Mencione ingredientes especiais**
- **Evite nomes muito longos**

### Precificar Inteligentemente
- **Pesquise a concorrência**
- **Considere o custo dos ingredientes**
- **Teste diferentes preços**
- **Ofereça opções para todos os bolsos**

### Descrever de Forma Atrativa
- **Use linguagem apetitosa**
- **Mencione benefícios**
- **Crie desejo**
- **Seja honesto sobre o produto**

### Organizar por Popularidade
- **Coloque produtos populares** como "gourmet"
- **Teste novos sabores** como "novo"
- **Mantenha clássicos** como "tradicional"

---

## 📞 Suporte Técnico

Se encontrar problemas que não consegue resolver:

1. **Anote exatamente** o que estava fazendo
2. **Tire uma foto** da tela se necessário
3. **Tente reproduzir** o problema
4. **Entre em contato** com o desenvolvedor

**Lembre-se**: Este manual cobre as funcionalidades principais. Para personalizações avançadas, consulte o arquivo README.md ou entre em contato com suporte técnico.

---

*Manual atualizado em Janeiro 2025*

