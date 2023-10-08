# Pomodoro Timer em Python
Este repositório contém um código Python que implementa um "Pomodoro Timer", uma técnica de gerenciamento de tempo que ajuda a melhorar a produtividade e a concentração por meio de intervalos de trabalho e pausas regulares. Este código pode ser usado para automatizar sessões de trabalho com base nas configurações fornecidas pelo usuário.

## Funcionalidade
### Pomodoro Timer
- O código implementa um temporizador Pomodoro que alterna entre sessões de trabalho e pausas.
- O usuário pode configurar o tempo de trabalho, o tempo de pausa curta, o tempo de pausa longa e o número de ciclos desejados.
- Durante cada ciclo, o código exibe contagens regressivas para o tempo de trabalho e pausa no terminal.
- Após o tempo de trabalho, o código limpa o terminal (compatível com Linux/macOS) para fornecer uma divisão visual entre sessões de trabalho e pausas.
- Após o tempo de pausa curta, o código volta à contagem regressiva do tempo de trabalho.
- Após o tempo de pausa longa (após um número específico de ciclos de trabalho), o código também executa uma contagem regressiva antes de retornar ao trabalho.
## Como Executar
### Requisitos
- Python instalado em seu ambiente de desenvolvimento.
### Passos
1. Clone ou faça o download deste repositório para o seu computador.
2. Abra um terminal ou prompt de comando.
3. Navegue até o diretório onde o código está localizado.
4. Execute o código Python usando o comando:
```
python main.py
```
1. O Pomodoro Timer iniciará com base nas configurações padrão (25 minutos de trabalho, 5 minutos de pausa curta, 15 minutos de pausa longa e 4 ciclos).
2. A contagem regressiva será exibida no terminal, e o código notificará quando for hora de trocar entre trabalho e pausa.
3. Você pode personalizar as configurações editando as variáveis tempo_trabalho, tempo_pausa_curta, tempo_pausa_longa, e ciclos no código-fonte.
<p>
  Lembre-se de que este é um exemplo simples de um Pomodoro Timer em Python. Você pode expandir ou personalizar o código de acordo com suas necessidades específicas e adicionar recursos adicionais, como notificações sonoras ou interfaces gráficas. Divirta-se usando o Pomodoro Timer para melhorar sua produtividade!
</p>
