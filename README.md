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