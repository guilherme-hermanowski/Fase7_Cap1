import streamlit as st
import pandas as pd
st.set_page_config(page_title='EstruturaDB',page_icon='',layout='wide')
st.title('Estrutura do Banco de Dados')
st.write('Na FarmTech Solutions temos um sistema de coleta de informacões no campo que funciona através de sensores que, ao receberem informacões, repassam ao nosso banco de dados. Dessa forma, é comum que surjam dúvidas de como é estruturado esse banco e é para isso que essa página serve. Nosso modelo de negócio consiste em um sistema de 3 sensores que monitoram uma determinada plantação. Sendo assim, criamos 3 elementos, um para cada sensor, os intitulamos de acordo e estruturados seus atributos da seguinte forma:')

with st.expander("Sensor PH"):
    st.info('cd_ph - int - (chave primaria)')
    st.info('cd_servidor - int (chave estrangeira)')
    st.info('ph_solo - float - (1, n)')
    st.info('data_ph - date - (1, n)')
    st.info('hora_ph - time - (1, n)')

st.markdown("""---""")

with st.expander("Sensor NPK"):            
    st.info('cd_NPK - int - (chave primaria)')
    st.info('cd_servidor - int - (chave estrangeira)')
    st.info('fosforo - float - (1, n)')
    st.info('potássio - float - (1, n)')
    st.info('ata_npk - date - (1, n)')
    st.info('hora_npk - time - (1, n)')

st.markdown("""---""")

            
with st.expander("Sensor Umidade"):
    st.info('cd_Umidade - int - (chave primária)')
    st.info('cd_servidor - int - (chave secundária)')
    st.info('umidade solo - float - (1, n)')
    st.info('umidade ar - float - (1, n)')
    st.info('temperatura - float - (1, n)')
    st.info('data umidade - date - (1, n)')
    st.info('hora umidade - time - (1, n)')

st.markdown("""---""")

with st.expander("Interface"):
    st.info("cd_interface - int - (chave primária)")
    st.info("cd_servidor - int - (chave estrangeira)")
    st.info("resultados - varchar100 - (0, n)")

st.markdown("""---""")

st.markdown("""
            
- Todos esses elementos possuem um relacionamento com o elemento servidor. Nomeado como recebimento de dados, esse relacionamento possui as cardinalidades (1, n) e (1, 1).

- O elemento servidor recebe como atributo, além de todos os dados contidos nos demais elementos, o dado cd_servidor, que é sua chave primária e utilizada como chave estrangeira nas outras entidades.

- Na sequência, as informações são processadas na entidade servidor e passadas a entidade interface através do relacionamento (1, 1) nomeado como dados.

- Por fim temos o elemento interface.""")

st.markdown("""---""")

st.subheader("Para melhor visualização, abaixo temos a imagem do DER:")

st.image("imagens/DER.png", caption="Diagrama Entidade-Relacionamento")

