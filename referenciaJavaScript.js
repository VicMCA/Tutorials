#!/usr/bin/env node

function main() {
    'Acima é o começo da função principal.'
    'Aqui também fica a mini-documentação da função'

    console.log('\nBem-vindo(a) ao guia rápido de "Como Fazer X" em JavaScript.')
    
    function sub() {
        console.log('\nAqui por exemplo, tem uma função dentro de outra. Veremos como fazer isso mais a frente.')
      }
    
      sub()
  }

if (require.main === module) {
    main();
  }