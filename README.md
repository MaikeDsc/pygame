
# 🌿 Sussurros da Selva

🎮 **Sussurros da Selva** é um jogo 2D de ação e aventura inspirado em clássicos como **Cuphead** e **Hollow Knight**.  
O jogador embarca em uma jornada pela misteriosa selva amazonica, enfrentando **chefes desafiadores** e provando sua coragem em meio a criaturas sombrias e sussurros da floresta.

---

## ⚔️ Desenvolvedores

-👾**Deyvison Rolim Sousa** 
<br></br>
-👾**Maquiavel dos Santos Campos** https://github.com/MaikeDsc
<br></br>
-👾**Daniel Sant'Anna de Araujo**  https://github.com/Sann1ck
</br></br>
-👾**Luiz Guilherme Barreto**
<br></br>

## 🐍 Enredo

Em uma selva esquecida pelo tempo, ecos de antigas civilizações ainda ressoam.  
Você é **Aranã**, um guardião que desperta em meio a selva para evitar a alatração de um mau maior.  
Sua missão é sobreviver às **três grandes lendas do folclore que estão corrompidas** — cada uma representando um aspecto da natureza — e restaurar o equilíbrio perdido da selva.

---

## ⚔️ Jogabilidade

- 🌲 **Três fases principais**, cada uma com um **boss único** e um **tema florestal**.  
- 🌀 **Sistema de combate dinâmico**, com ataques a distância e habilidades especiais.  
- 🦋 **Estilo artístico desenhado à mão**, remetendo a animações retrô.  
- 💀 **Dificuldade desafiadora**, exigindo reflexos e estratégia para sobreviver.

---

## ⚔️ Sobre a pasta Shooter Maike

- 🔫 **Foi um estudo previo** na qual foi trabalhado algumas mecanicas de gameplay durante a aprendizagem sobre o pygame, tais mecanicas podem ser testasdas ou usadas para o projeto Sussuros da Salva, o codigo da pasta shooter pode ser alterado livremente para testes ou visualizações rapidas.  


---


## Comandos basicos do git  

git init
-> inicializar o GIT

git config --global user.name "nameuser" 
git config --global user.gmail "name@gmail.com"  
 -> configuração do GIT

git add .
git arquivo.type 
 -> Adicionar o arquivo no Git 

git commit -m "mensagem"
 -> criar uma versão para o projeto atual com uma
 mensagem associada

 git commit -ammend -m "mensagem"
 -> altera o ultimo commit
 -> Use quando esquece de Adicionar algo no ultimo commit

git status 
 -> mostra o estado atual do repositório

git log
 -> exibi o histórico dos commits

git branch @Ramifiação@
 -> lista todas branchs
 -m renomeia o nome da branch atual

git checkout 
 -> usada para acessar branch e commits pela hash
 -b criar e acessa uma nova branch

git remote add origin https://github.com/username/nome-do-repositorio.git
 ou 
git remote set-url origin https://username:token@github.com/username/nome-do-repositorio.git
 -> cria uma conexão remota com o repositório especificado
git remote -v 
-> lista todos os repositorios vinculados ao seu projeto com suas URLs

git push -u origin master
 -> envia a commit para o repositório do GitHub
 -u rastreia o repositorio remoto e torna padrão
 
git clone "url"
 -> clona o repositorio remoto para ambiente local 

git pull origin main
-> baixa as mudanças feitas para repositorio atual

git reset --hard <hash_do_commit_anterior>
-> apaga um commit

git pull --rebase origin master
(ja faz o trabalho do pull e fetch)

vai atualizar o teu repositório local, caso eu ja tenha mexido algo.
basta esse. depois pode dar add e commit
(mas por cautela pode executar esse de --rebase novamente antes de dar push)

