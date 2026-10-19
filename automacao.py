from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# ==========================================
# 1. CONFIGURAÇÕES DO CHROME
# ==========================================
chrome_options = Options()

# Mantém a janela aberta após o término
chrome_options.add_experimental_option("detach", True)

# Oculta avisos de automação do Selenium
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# Desativa o gerenciador de senhas
chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})

# Desativa telas e pop-ups nativos do Chrome
chrome_options.add_argument("--disable-signin-promo")
chrome_options.add_argument("--no-first-run")
chrome_options.add_argument("--no-default-browser-check")

# Rodar em modo anônimo para evitar telas de perfil do Chrome
chrome_options.add_argument("--incognito")

# ==========================================
# 2. INICIALIZAÇÃO DO NAVEGADOR
# ==========================================
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)
driver.maximize_window()

# ==========================================
# 3. ETAPA 1: LOGIN NO GOOGLE
# ==========================================
driver.get("https://mail.google.com/")

# Preenche o e-mail no Google
campo_email = driver.find_element(By.ID, "identifierId")
campo_email.send_keys("***********")  # <-- Insira seu email ou CPF aqui


time.sleep(2)


# Clica em Avançar
botao_avancar = driver.find_element(By.ID, "identifierNext")
botao_avancar.click()

# ==========================================
# 4. ETAPA 2: REDIRECIONAMENTO E LOGIN NO SENAI
# ==========================================
time.sleep(4)  # Aguarda o carregamento do portal SENAI

# Preenche o e-mail no SENAI
campo_senai_email = driver.find_element(By.XPATH, "//input[@placeholder='Digite seu e-mail ou CPF']")
campo_senai_email.click()
campo_senai_email.send_keys("********") # <-- Insira seu email ou CPF aqui

time.sleep(3)

# Preenche a senha no SENAI
campo_senai_senha = driver.find_element(By.XPATH, "//input[@placeholder='Digite sua senha']")
campo_senai_senha.click()
campo_senai_senha.send_keys("*******")  # <-- Insira sua senha aqui

# Clica no botão Entrar
botao_entrar = driver.find_element(By.XPATH, "//button[contains(text(), 'Entrar')]")
botao_entrar.click()

print("Login enviado com sucesso!")




# ==========================================
# 5. ETAPA 3: ABRIR NOVA GUIA E ACESSAR O CLASSROOM
# ==========================================
time.sleep(7)  # Aguarda a conclusão do login do Gmail


# 1. Executa um script em JavaScript para abrir uma aba em branco
driver.execute_script("window.open('');")

# 2. Alterna o controle do Selenium para a nova aba (a última da lista)
driver.switch_to.window(driver.window_handles[-1])

time.sleep(6)


# 3. Acesse o Google Classroom na nova aba
driver.get("https://classroom.google.com/")

time.sleep(2)

print("Google Classroom aberto na nova guia com sucesso!")