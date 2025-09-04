# Guia de Instalação - Backend Bendito Docce

Este guia fornece instruções passo a passo para instalar e configurar o backend da Bendito Docce em sua máquina local.

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter os seguintes softwares instalados:

### 1. Python 3.8 ou superior
- **Windows**: Baixe em https://python.org/downloads/
- **macOS**: Use Homebrew: `brew install python3`
- **Linux**: Use o gerenciador de pacotes: `sudo apt install python3 python3-pip`

### 2. MySQL Server 8.0 ou superior
- **Windows/macOS**: Baixe em https://dev.mysql.com/downloads/mysql/
- **Linux**: `sudo apt install mysql-server`

### 3. MySQL Workbench (Opcional)
- Baixe em https://dev.mysql.com/downloads/workbench/
- Facilita o gerenciamento visual do banco de dados

## 🗄️ Configuração do Banco de Dados

### Passo 1: Iniciar o MySQL Server

**Windows:**
- Inicie o serviço MySQL pelo Painel de Controle > Serviços
- Ou use o MySQL Workbench para conectar

**macOS:**
```bash
sudo /usr/local/mysql/support-files/mysql.server start
```

**Linux:**
```bash
sudo systemctl start mysql
sudo systemctl enable mysql
```

### Passo 2: Criar o Banco de Dados

1. **Conecte-se ao MySQL**:
   ```bash
   mysql -u root -p
   ```

2. **Crie o banco de dados**:
   ```sql
   CREATE DATABASE bendito_docce_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

3. **Crie um usuário específico (Recomendado)**:
   ```sql
   CREATE USER 'bendito_user'@'localhost' IDENTIFIED BY 'senha_segura';
   GRANT ALL PRIVILEGES ON bendito_docce_db.* TO 'bendito_user'@'localhost';
   FLUSH PRIVILEGES;
   EXIT;
   ```

### Passo 3: Testar a Conexão
```bash
mysql -u bendito_user -p bendito_docce_db
```

## 🐍 Configuração do Backend

### Passo 1: Extrair o Projeto
1. Extraia o arquivo ZIP do backend
2. Navegue até o diretório:
   ```bash
   cd bendito-docce-backend
   ```

### Passo 2: Ativar o Ambiente Virtual

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

Você deve ver `(venv)` no início do prompt do terminal.

### Passo 3: Instalar Dependências
```bash
pip install -r requirements.txt
```

### Passo 4: Configurar Credenciais do Banco

**Opção A: Editar o arquivo de configuração**
1. Abra `src/config.py`
2. Modifique as credenciais:
   ```python
   MYSQL_HOST = 'localhost'
   MYSQL_PORT = 3306
   MYSQL_USER = 'bendito_user'  # ou 'root'
   MYSQL_PASSWORD = 'sua_senha'
   MYSQL_DATABASE = 'bendito_docce_db'
   ```

**Opção B: Usar variáveis de ambiente**
```bash
export MYSQL_HOST=localhost
export MYSQL_PORT=3306
export MYSQL_USER=bendito_user
export MYSQL_PASSWORD=sua_senha
export MYSQL_DATABASE=bendito_docce_db
```

## 🚀 Executando o Backend

### Passo 1: Iniciar o Servidor
```bash
python src/main.py
```

### Passo 2: Verificar se está Funcionando
1. Abra o navegador
2. Acesse: `http://localhost:5000`
3. Você deve ver o site da Bendito Docce

### Passo 3: Inicializar Dados de Exemplo (Opcional)
Para popular o banco com produtos de exemplo:

1. **Via navegador**: Acesse `http://localhost:5000/api/init-data` (método POST)
2. **Via curl**:
   ```bash
   curl -X POST http://localhost:5000/api/init-data
   ```

## 🧪 Testando a API

### Testar Endpoints com curl

**Listar produtos:**
```bash
curl http://localhost:5000/api/products
```

**Listar categorias:**
```bash
curl http://localhost:5000/api/categories
```

**Criar um produto:**
```bash
curl -X POST http://localhost:5000/api/products \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Brigadeiro Teste",
    "description": "Produto de teste",
    "price": 4.00,
    "category_id": 1,
    "image_url": "teste.jpg"
  }'
```

### Testar com Postman
1. Importe a coleção de endpoints
2. Configure a base URL: `http://localhost:5000`
3. Teste todos os endpoints CRUD

## 🔧 Solução de Problemas Comuns

### Erro: "Can't connect to MySQL server"
**Causa**: MySQL Server não está rodando ou credenciais incorretas.

**Soluções**:
1. Verifique se o MySQL está rodando:
   ```bash
   # Linux/macOS
   sudo systemctl status mysql
   
   # Windows - verifique nos Serviços
   ```

2. Teste a conexão manualmente:
   ```bash
   mysql -h localhost -u root -p
   ```

3. Verifique as credenciais no `config.py`

### Erro: "ModuleNotFoundError"
**Causa**: Ambiente virtual não ativado ou dependências não instaladas.

**Soluções**:
1. Ative o ambiente virtual:
   ```bash
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

2. Reinstale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

### Erro: "Port 5000 already in use"
**Causa**: Outra aplicação está usando a porta 5000.

**Soluções**:
1. Pare outros serviços na porta 5000
2. Ou modifique a porta no `main.py`:
   ```python
   app.run(host='0.0.0.0', port=5001, debug=True)
   ```

### Erro: "Access denied for user"
**Causa**: Credenciais do MySQL incorretas.

**Soluções**:
1. Verifique o usuário e senha
2. Confirme as permissões do usuário:
   ```sql
   SHOW GRANTS FOR 'bendito_user'@'localhost';
   ```

## 📱 Acessando de Outros Dispositivos

Para acessar o backend de outros dispositivos na mesma rede:

1. **Descubra seu IP local**:
   ```bash
   # Linux/macOS
   ifconfig | grep inet
   
   # Windows
   ipconfig
   ```

2. **Acesse via IP**: `http://SEU_IP:5000`

3. **Configure o firewall** se necessário para permitir conexões na porta 5000

## 🔒 Configurações de Segurança

### Para Ambiente de Produção
1. **Altere a SECRET_KEY**:
   ```python
   SECRET_KEY = 'sua-chave-super-secreta-aqui'
   ```

2. **Desabilite o modo DEBUG**:
   ```python
   app.run(host='0.0.0.0', port=5000, debug=False)
   ```

3. **Use HTTPS** em produção

4. **Configure CORS** para domínios específicos:
   ```python
   CORS(app, origins=["https://seudominio.com"])
   ```

## 📞 Suporte Adicional

Se você encontrar problemas não cobertos neste guia:

1. **Verifique os logs** do Flask no terminal
2. **Teste cada componente** separadamente (Python, MySQL, dependências)
3. **Consulte a documentação** oficial do Flask e MySQL
4. **Verifique as versões** dos softwares instalados

## ✅ Checklist de Instalação

- [ ] Python 3.8+ instalado
- [ ] MySQL Server instalado e rodando
- [ ] Banco de dados `bendito_docce_db` criado
- [ ] Usuário MySQL configurado
- [ ] Ambiente virtual ativado
- [ ] Dependências instaladas
- [ ] Credenciais configuradas
- [ ] Backend rodando em `http://localhost:5000`
- [ ] Site carregando no navegador
- [ ] APIs respondendo corretamente

Parabéns! Seu backend da Bendito Docce está pronto para uso! 🎉

