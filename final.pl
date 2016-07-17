%que pondremos aqui?

tipo_palabras(colericas).
tipo_palabras(melancolicas,Palabras).
tipo_palabras(sanguineas,Palabras).
tipo_palabras(flematicas,Palabras).

persona("jesus",[]).

main :-
    open('final.txt', read, Str),
    read_file(Str,Lines),
    close(Str),
    write(Lines), nl.

read_file(Stream,[]) :-
    at_end_of_stream(Stream).

read_file(Stream,[X|L]) :-
    \+ at_end_of_stream(Stream),
    read(Stream,X),
    read_file(Stream,L).

palabra() :- read(Palabra),
	   open('sanguineas.txt', read, Str),
	           read_file(Str,Lines),!,
		    not(member(Palabra,Lines)),
			write("N/A").
		   
palabra() :- read(Palabra),
	   open('sanguineas.txt', read, Str),
	           read_file(Str,Lines),
		   close(Str),
		   write(Lines),
		   member(Palabra,Lines),
		   write("Sanguineo").
		   
		   