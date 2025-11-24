import streamlit as st
import pandas as pd
st.set_page_config(page_title='EstruturaSensor',page_icon='',layout='wide')
st.title('Funcionamento dos Sensores')
st.write('Como citado anteriormente, a FarmTech Solutions temos um sistema de coleta de informacões no campo que funciona através de sensores. Estes sensores são conectados a um microcontrolador ESP32, que por sua vez, faz a leitura dessas informações e repassa para o banco. Segue componentes e lógica de funcionamento:')

with st.expander('⚙️ Componentes e Conexões'):
    st.markdown("""- **Sensor Fosforo - Botão Vermelho**:
  - Conexão: pino 23

---

- **Sensor Potassio - Botão Verde**:  
  - Conexão: pino 22

---

- **Sensor Ph - Sensor LDR**: 
  - Conexão: 35
  - Responsável por simular a coleta do PH.

---

- **Sensor Temperatura e Umidade - Sensor DHT22**: 
  - Conexão: 15
  - Responsável por coleta de temperatura e umidade.

---

- **Sensor Bomba Irrigação - LED (Vermelho e Verde) (Relé simulado)**: 
  - Conexão: pino 2
  - Utilizado como atuador da bomba de irrigação.""")
    
with st.expander('🧠 Lógica de Funcionamento'):
    st.markdown("""- **Observações:**
  - Segundo a liberdade e criatividade da lógica de coleta dos sensores, definimos que o para a simulação, o sistema evita logs repetitivos: só gera nova saída quando há mudança no estado dos sensores **LDR (Ph), Botões (Fosforo e Potassio)**.
  - A coleta do sensor de Temperatura e Umidade é mostrado toda vez que há alterações em alguns desses sensores (para não poluir o monitor e também facilitar validação da avaliação.
  - A coleta do sensor do Relé, simulando a bomba de irrigação é feita automaticamente só com a alteração de umidade no sensor DTH22.
  - O valor de pH é tratado com `fabs()` para considerar desvios mínimos.
  - Ao final do Loop com alteração de parametros do sensor LDR ou botão, o log é gerado coletando de todos os sensores (até os que não foram alterados, para gerar carga na cópia para execução do entregável 2) - Simulando uma Trigger para disparo de log / coleta

- O sistema lê os botões de **fósforo** e **potássio**. Quando pressionados, gera valores aleatórios simulando a presença em mol desses nutrientes.
- O valor de **pH** é calculado com base em um valor analógico lido pelo sensor LDR
- O sensor DHT22 fornece leitura de **temperatura** e **umidade**.
- A **bomba de irrigação (LED)** é acionada ou desligada conforme o valor da umidade:
  - **≥ 40%**: bomba desligada (LED Vermelho Ligado)
  - **< 40%**: bomba ligada (LED Verde Ligado)
- Todos os dados são exibidos no monitor serial, com um bloco especialmente formatado para facilitar a cópia e posterior uso em scripts Python
""")

with st.expander('📤 Exemplo de Saída no Serial'):
    st.markdown("""```
Presença Fosforo: 68.32
Presença Potassio: 92.14
Ph: 5.89
Temp (°C): 23.55
Humidity (%): 35.7

============================================ COPIAVEL PARA SCRIPT PYTHON ============================================

log,68.32,92.14,5.89,23.55,35.7

**Sendo (seria a data no projeto real por exemplo), (Fosforo), (Potassio), (Ph), (Temp), (Umidade)

=====================================================================================================================
```
""")

with st.expander('⚡Circuito'):
    st.image('imagens/Circuito_Wokwi.png', caption='Diagrama de Circuito simulado no Wokwi')

import streamlit as st
import requests

# --------------------------------------------
# Função para disparar alerta via API Gateway
# --------------------------------------------
def disparar_alerta(mensagem: str):
    url = "https://nhcefqu3vh.execute-api.sa-east-1.amazonaws.com/disparos"

    payload = {"mensagem": mensagem}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers)

        return {
            "status": response.status_code,
            "body": response.text
        }

    except requests.exceptions.RequestException as e:
        return {
            "status": "erro",
            "body": str(e)
        }


# --------------------------------------------
# Página Streamlit (sem set_page_config)
# --------------------------------------------
st.title("🚨 Disparo de Alertas via API Gateway")
st.write("Preencha a mensagem abaixo e clique em **Enviar alerta** para disparar via API.")

# Entrada da mensagem
mensagem = st.text_area("Mensagem do alerta", height=150)

# Botão para enviar alerta
if st.button("Enviar alerta"):
    if not mensagem.strip():
        st.error("Por favor, escreva uma mensagem antes de enviar.")
    else:
        with st.spinner("Enviando alerta para a API..."):
            resultado = disparar_alerta(mensagem)

        # Exibe resultado
        st.subheader("📡 Resultado da API")
        st.write(f"**Status:** {resultado['status']}")
        st.code(resultado["body"], language="json")
