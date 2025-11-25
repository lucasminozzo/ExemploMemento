Atividade proposta:

Objetivo: Implementar um sistema de "checkpoint" para um jogo simples usando o padrão Memento.

Cenário: Você está criando um jogo de aventura. O seu Jogador tem atributos como vida, mana e posicao (x, y). O jogador precisa ser capaz de salvar seu progresso em "checkpoints" e, se ele "morrer" (perder toda a vida), ele deve ser capaz de carregar o último checkpoint salvo.

O Problema: O sistema de "save" (o GerenciadorDeSaves) precisa armazenar o estado do jogador, mas ele não deve ter permissão para acessar ou modificar diretamente os atributos privados do Jogador (como jogador._vida = 100). Isso violaria o encapsulamento.

Sua Tarefa: Implemente as alterações necessárias para o padrão Memento (Jogador, SaveState, GerenciadorDeSaves) e o fluxo para salvar e carregar o jogo.
