  
###### Placeholder para o projeto. Realoquei as istruções dgit how to" para cá.

Instruções para git
*   Em arquivos markdown, espaço duplo pula linha "  "  
*   Use estrela única para itálico, dupla para bold, tripla para itálico + bold  
*   Coisas entre acento grave ` são código  

|>>  `git init`  
*   Inicializa git na pasta atualmente selecionada*  

|>>  `git add "arquivo.extensão"` *(executar sem aspas)*  
*   Adiciona o arquivo para a monitoração de mudanças  

|>>  `git status`  
*   Verifica o status atual git, mudanças que ocorreram, commits, etc  

|>>  `git commit -m "mensagem"`  
*   Realiza o commit dos arquivos, com uma mensagem descrevendo o commit  

|>>  `git branch -M "main"`  
*   Muda o nome da branch para o nome entre aspas  

|>>  `git remote add origin https://github.com/usuário/pasta.git`  
*   Apelida a pasta atual como "origin" e a conecta com a pasta selecionada no GitHub  

|>> `git remote set-url origin https://github.com/usuário/pasta.git` 
*   Muda o endereço de "origin", útil para caso o projeto já tenha um origin anteriormente  
*   e você queira redirecionar (caso você tenha clonado de alguém, por exemplo)  

|>> `git remote -v`  
*   Confere os endereços online conectados à pasta atual do projeto no computador  

|>> `git remote remove apelido-da-pasta`  
*   Remove o apelido selecionado para a conexão com o repositório no github. Pode ser origin ou outro

|>>  `git push -u origin main`  
*   Envia os arquivos de 'origin' para 'main' da primeira vez. Depois dela, use como abaixo  
|>>  `git push origin main`  

|>> `git push origin nova-branch`  
*   Envia os arquivos para a branch selecionada, neste caso é a 'nova-branch'  

|>> `git checkout -b "nome-da-nova-branch"`  
*   Cria e entra em uma nova branch do projeto  

|>> `git checkout main`  
*   Volta para a branch "main"  

|>> `git merge nova-feature`  
*   Traz o conteúdo da branch "nova-feature" para a branch "main"  

|>> `git clone https://github.com/perfil-do-usuario/repositorio-a-ser-puxado.git`  
*   Clona o repositório do endereço e o coloca na pasta onde você estiver (ex: usuario/docs/ a pasta conada fica aqui)  

|>> `git pull`  
*   Baixa do github as atualizações para a pasta no computador  
