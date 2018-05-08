def is_stressful(subj):
    import re
    red = [re.compile(red) for red in
           ["H\W*E\W*L\W*P","A\W*S\W*A\W*P","U\W*R\W*G\W*E\W*N\W*T",
            "H+E+L+P+","A+S+A+P+","U+R+G+E+N+T+"]]
    return any([subj == subj.upper(),subj[-3:] == "!!!",
                any([re.search(word, subj.upper()) for word in red])])
