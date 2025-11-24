import streamlit as st
import pandas as pd

st.title('🧠 Visão Computacional com YOLOv5')

st.markdown(''' ### Essa aba demonstra os resultados da aplicação de um sistema de visão computacional usando YOLOv5, com foco em dois objetos distintos: **cat** e **bike**. O objetivo é treinar um modelo capaz de identificar esses objetos com alta acurácia, validando seu uso em cenários reais da FarmTech Solutions.

---''')

st.header('Etapas')
st.markdown("""
 ##### 1. Preparação do Ambiente
 ##### 2. Organização do Dataset
 ##### 3. Treinamento do Modelo
 ##### 4. Métricas a comparar ['mAP@0.5', 'Precisão', 'Revocação', 'Box Loss', 'Obj Loss', 'Cls Loss']
 ##### 5. Comparação: mAP@0.5
 ##### 6. Gráficos Comparação: Box loss, Cls Loss, mAP@0.5, Obj Loss, Precisão, Revocação
 ##### 7. Gráficos exportados para: /content/drive/MyDrive/FarmTechVision_Grupo7/YOLOv5_Graficos
 ##### 8. Exportar imagens para o Google Drive
 ##### 9.  Resultados Visuais
 ##### 10. Conclusões

---""")

st.warning('### **Observação:**\n ##### Por motivos de performance e visando menor carga de máquinas locaisodo este código foi executado via Google Colab. Sendo assim, está página tem o intuito de apresentar os resultado e insights extraidos dessa avaliação.\n ##### Caso queira ter acesso a toda documentação do projeto, você pode encontrar todos os links na caixa abaixo. \n')

with st.expander('🌐 Links'):
    st.info('##### [Google Colab](https://colab.research.google.com/drive/17r-pJUDiiel7gbe-Dt6pAYz_TpRnsdoh)\n' \
    '##### [Dataset de 30 épocas](https://drive.google.com/drive/folders/1GNTK54SlLoN4LtkTbNyjCNbWyLFeVwhP)\n' \
    '##### [Dataset de 60 épocas](https://drive.google.com/drive/folders/1lrif1HiMNxfmbBn5fnEBiN4T8EeIdDIK)')

st.markdown('''---''')

st.header('Comparações Gráficas')
st.write('#### Após a execução dos codigos e treinamento dos modelos de 30 e de 60 épocas, conseguimos extrair os seguintes insights:\n')
st.image('imagens/comparacao_map@0.5.png', caption='Comparacão mAP@0.5\n')
st.image('imagens/comparacao_boxloss.png', caption='Comparacão Box Loss\n')
st.image('imagens/comparacao_clsloss.png', caption='Comparacão Cls Loss\n')
st.image('imagens/comparacao_objloss.png', caption='Comparacão Obj Loss\n')
st.image('imagens/comparacao_precisao.png', caption='Comparacão Precisão\n')
st.image('imagens/comparacao_revocacao.png', caption='Comparacão Revocação\n')

st.markdown('---')

st.markdown("""#### 📊 Análise Técnica dos Gráficos de Treinamento e Validação – YOLOv5 - “detect_60epocas”

Os gráficos gerados durante o treinamento do modelo YOLOv5 fornecem insights valiosos sobre o comportamento do modelo ao longo das épocas.
A seguir, apresentamos uma análise detalhada das principais métricas
observadas:

---

#### 📉 Perdas de Treinamento (`train/box_loss`, `train/obj_loss`, `train/cls_loss`) - “detect_60epocas”

As curvas de perda de treinamento mostram uma **tendência decrescente consistente**, indicando que o modelo está aprendendo a representar
melhor os objetos ao longo das épocas. A perda de caixa (`box_loss`) teve uma
queda significativa nas primeiras épocas e estabilizou em valores baixos, o que
é desejável. As perdas de objeto (`obj_loss`) e de classe (`cls_loss`) também
diminuíram progressivamente, sugerindo que o modelo está se ajustando bem às
tarefas de detecção e classificação.

---

#### 📉 **Perdas de Validação (`val/box_loss`, `val/obj_loss`,**

#### `val/cls_loss`) - “detect_60epocas”

As perdas de validação seguiram uma tendência semelhante às de treinamento, com **valores próximos e estáveis**, o que indica que o modelo está generalizando bem para dados que ele nunca viu. Não há sinais evidentes de overfitting, já que as perdas não aumentaram nas últimas épocas.

---

#### 🎯 **Métricas de Precisão e Revocação (`metrics/precision`,**

#### metrics/recall`) - “detect_60epocas”

A **precisão** apresentou crescimento ao longo das épocas, estabilizando em valores próximos de **0.9**, o que indica que o modelo está fazendo predições corretas com baixa taxa de falsos positivos. A **revocação ** atingiu valores próximos de **1.0**, mostrando que o modelo está conseguindo detectar praticamente todos os objetos presentes nas imagens.

---

#### 📈 Precisão Média (`metrics/mAP_0.5` e  `metrics/mAP_0.5:0.95`)

A métrica `mAP@0.5` ultrapassou **0.98**, o que representa um desempenho excelente em termos de detecção com IoU ≥ 0.5. Já o `mAP@0.5:0.95`, que é uma métrica mais exigente, atingiu valores superiores a **0.54**, indicando que o modelo também está performando bem em múltiplos níveis de sobreposição entre predições e objetos reais.

---

#### 📈 Interpretação Geral “detect_60epocas”

- O modelo apresentou **aprendizado consistente**, com perdas decrescentes e métricas de desempenho crescentes.

- A **estabilização das curvas** nas últimas épocas sugere que o modelo atingiu um bom ponto de convergência.

- A **ausência de divergência entre treino e validação** reforça a qualidade do dataset e a eficácia do treinamento.

- As métricas finais indicam que o modelo está **pronto para ser testado em cenários reais**, com alta confiabilidade na detecção de objetos.

****

Esses resultados demonstram que o treinamento foi bem-sucedido e que o modelo YOLOv5 está apto para aplicações práticas em visão computacional, como segurança patrimonial, monitoramento animal ou controle de acesso em ambientes rurais e urbanos.

#### 🔄 **Comparação entre Treinamentos com 30 e 60 Épocas – YOLOv5**

Realizamos dois treinamentos distintos com o modelo YOLOv5, utilizando o mesmo dataset, mas variando a quantidade de épocas: 30 e 60. A seguir, apresentamos uma análise comparativa das principais métricas de desempenho.

#### 📈 **Métricas de Avaliação**

| **Métrica**       | **30 Épocas** | **60 Épocas** | **Diferença** |
| ----------------- | ------------- | ------------- | ------------- |
| **Precisão (P)**  | 0.87          | 0.93          | +0.06         |
| **Revocação (R)** | 1.00          | 1.00          | =             |
| **mAP@0.5**       | 0.982         | 0.995         | +0.013        |
| **mAP@0.5:0.95**  | 0.544         | 0.612         | +0.068        |
| **Perda total**   | 0.0412        | 0.0362        | –0.005        |

#### 📈 Resultados Visuais

Segue estão os prints das imagens de teste processadas pelo modelo, com as detecções realizadas.""")

st.image("imagens/30-60_Epocas.png", caption='Representação Visual') 

st.markdown("""
#### 📈 Interpretação

- O modelo treinado com **60 épocas** apresentou **melhor desempenho em todas as
  métricas**, especialmente em mAP@0.5:0.95, que é mais exigente.

- A **perda total foi menor**, indicando que o modelo aprendeu melhor a representar
  os objetos.

- Ambos os modelos atingiram **revocação máxima (1.00)**, mas o de 60 épocas teve
  **maior precisão**, o que significa menos falsos positivos.

- A evolução entre os dois treinamentos mostra que o modelo continua aprendendo após 30 épocas, sem sinais de overfitting.

- Treinamentos mais longos resultam em modelos mais precisos e robustos. Para aplicações reais em visão computacional, recomenda-se utilizar pelo menos **60 épocas** para maximizar o desempenho.

#### 📈 **Conclusões**

- Modelo com 60 épocas teve melhor desempenho

- Sistema viável para aplicações reais

- O modelo com 60 épocas apresentou melhor
  desempenho geral.

- O sistema é viável para aplicações reais da FarmTech Solutions, como segurança
  patrimonial e controle de acessos.

- A limitação principal foi o tamanho reduzido do dataset, que pode ser expandido
  em versões futuras.
                        
""")

st.header('Conclusões Finais')
st.markdown('''
##### - O modelo com 60 épocas apresentou maior acurácia e menor erro de detecção.
##### - O tempo de treinamento foi maior, mas compensado pela qualidade dos resultados.
##### - O sistema demonstrou potencial para ser aplicado em cenários reais da FarmTech Solutions, como segurança patrimonial e controle de acessos.''')

st.header('Limitações:')
st.markdown('''##### - Dataset pequeno pode limitar a generalização.
##### - Imagens com baixa qualidade ou iluminação prejudicam a detecção.''')