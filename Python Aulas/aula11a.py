"""
**************************************************
AULA 11
**************************************************

        Código ANSI
        Escape Sequence
        \033[style;text;backm          ex: \033[0;33;44m

        style                       text                    back
        0       none                30      black           40      black
        1       bold                31      red             41      red
        4       underline           32      green           42      green
        7       negative            33      yellow          43      yellow
                                    34      blue            44      blue
                                    35      magenta         45      magenta
                                    36      cyan            46      cyan
                                    37      gray            47      gray
                                    97      white          107      white

"""

print('\033[1;30;107mOlá, Mundo!\033[m')

