import pandas as pd
import streamlit as st
import csv
import random
from time import sleep



##### Funções__________________________________________________________________________________________________
def DefineFaixa(): #cria arquivo csv com a faixa de números para o sorteio
    with open ('learn_csv.csv', 'w', newline='') as csvfile:
        ApagaFaixa = csv.writer(csvfile, delimiter=',')
        ApagaFaixa.writerow([])
    with open ('learn_csv2.csv', 'w', newline='') as csvfile:
        ApagaSorteados = csv.writer(csvfile, delimiter=',')
        ApagaSorteados.writerow([])
    with open('learn_csv.csv','a', newline='') as scvfile:
        for i in range(1,ValorMaximo+1):
           defFaixa=csv.writer(scvfile, delimiter=',')
           defFaixa.writerow([str(i)])
    return

def RealizaSorteio(): #lê a faixa de números do arquivo csv, realiza sorteio e salva na lista scv de sorteados.
    
    with open ('learn_csv.csv','r', newline='') as scvfile:
        listaProv = csv.reader(scvfile, delimiter=",")
        listaFaixa=[]
        try:
            for linha in listaProv:
                for elemento in linha:
                    if (elemento != ""):
                        listaFaixa.append(int(elemento))
            
            NumSorteado = random.randint(listaFaixa[0], listaFaixa[-1])
            with open('learn_csv2.csv','a', newline='') as scvfile:
                gravaSorteado = csv.writer(scvfile, delimiter=',')
                gravaSorteado.writerow([str(NumSorteado)])
                        
                            
        
            with col2:
                with st.spinner("Aguarde... Realizando Sorteio..."):
                        sleep(1)
                        st.subheader(":blue[O número sorteado foi: ] :red["+ str(NumSorteado) + "]")
                
        except:
            st.error("Não foi possível completar a operação. Faixa de números para o sorteio não foi definida.")
            
            st.button("Atualizar página", on_click=st.experimental_rerun)
            st.stop()
        scvfile.close()
    return NumSorteado

def ReiniciaSorteio(): #lima os arquivos csv (faixa e numeros sorteados)
    with open ('learn_csv.csv', 'w', newline='') as csvfile:
        ApagaFaixa = csv.writer(csvfile, delimiter=',')
        ApagaFaixa.writerow([''])
    with open ('learn_csv2.csv', 'w', newline='') as csvfile:
        ApagaSorteados = csv.writer(csvfile, delimiter=',')
        ApagaSorteados.writerow([''])
    
    return


##### Execuções_______________________________________________________________________________________________________

st.subheader('Defina a faixa de números para este sorteio:')
ValorMaximo = st.slider(' ',min_value=1,max_value=1000)
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    tabela1=pd.read_csv('learn_csv.csv', sep=',', names=["Números para este sorteio"])
    tabela1Formtada = pd.DataFrame(tabela1)
    st.data_editor(tabela1Formtada, hide_index=True)
   

with col3:
    tabela2=pd.read_csv('learn_csv2.csv', sep=',', names=['Números sorteados'])
    tabela2Formtada = pd.DataFrame(tabela2)
    st.data_editor(tabela2Formtada,column_config={})
    

####Botões ___________________________________________________________________________________________
But1=st.sidebar.button('Definir Faixa', on_click=DefineFaixa, )
But2=st.sidebar.button('Realizar Sorteio', on_click=RealizaSorteio)
But3=st.sidebar.button('Reiniciar Sorteio', on_click=ReiniciaSorteio)

