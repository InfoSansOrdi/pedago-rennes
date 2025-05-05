


type tuile = int 
(*binary :
4 times : 	
1 bit of signature
two bits for the color
convention NSEO / HBDG
-1 = vide (ça passe j'utilise que 12 bits)
*)

type board = int array array

let rotate_left (t : tuile ) : tuile =
	(*OUEST -> SUD*) 	((0b1111 land t) lsl 8)
	(*EST -> NORD*) 	lor ((0b11110000 land t) lsl 8)
	(*SUD -> EST*)  	lor ((0b111100000000 land t) lsr 4)
	(*NORD -> OUEST*)	lor ((0b1111000000000000 land t) lsr 12)

let n = 6
let m = 4

let is_placeable (b : board) (i : int) (j : int) (t : tuile) : bool =  
	(**cette fonction travaille sur un tore
	on a pas trouvé de solutions dans ce cadre*)
	( (*NORD*)
		(
			(b.(i).((j-1+m) mod m) <> -1) 
			&& (((b.(i).((j-1+m) mod m) land   0b0000011100000000) lsr 8 ) = ((t land 0b0111000000000000) lsr 12))
			(*&& (((b.(i).((j-1+m) mod m) lxor t ) land 0b0000100000000000) = 0b1000000000000000)*)
		) || (b.(i).((j-1+m) mod m) = -1)
	)
	&& 
	( (*SUD*)
		(
			(b.(i).((j+1+m) mod m) <> -1) 
			&& (((b.(i).((j+1+m) mod m) land   0b0111000000000000) lsr 12) = ((t land 0b0000011100000000) lsr 8))
			(*&& (((b.(i).((j+1+m) mod m) lxor t ) land 0b1000000000000000) = 0b0000100000000000)*)
		) || (b.(i).((j+1+m) mod m) = -1) 
	) 
	&&
	( (*EST*)
		(
			(b.((i+1+n) mod n).(j) <> -1) 
			&& (((b.((i+1+n) mod n).(j) land   0b0000000000000111) lsr 0 ) = ((t land 0b0000000001110000) lsr 4))
			(*&& (((b.((i+1+n) mod n).(j) lxor t ) land 0b0000000000001000) = 0b0000000010000000)*)
	 	) || (b.((i+1+n) mod n).(j) = -1)
	)
	&&
	( (*OUEST*)
		(
			(b.(((i-1+n) mod n)).(j) <> -1) 
			&& (((b.(((i-1+n) mod n)).(j) land   0b0000000001110000) lsr 4 ) = ((t land 0b0000000000000111) lsr 0))
			(*&& (((b.(((i-1+n) mod n)).(j) lxor t ) land 0b0000000010000000) = 0b0000000000001000)*)
		) || (b.(((i-1+n) mod n)).(j) = -1)
	)

let is_placeable_non_tore (b : board) (i : int) (j : int) (t : tuile) : bool =  
	(**Ne travaille pas sur un tore. avec les points, il devrait y avoir 2 solutions.*)
	( (*NORD*)
		if (j <> 0) then 
		(
			(b.(i).(j-1) <> -1) 
			(*la première ligne fait la couleur, la seconde les points.*)
			&& (((b.(i).(j-1) land 0b0000011100000000) lsr 8 ) = ((t land 0b0111000000000000) lsr 12))
			&& (((b.(i).(j-1) land 0b0000100000000000) lsr 8 ) <>((t land 0b1000000000000000) lsr 12))
		) 	|| (b.(i).(j-1) = -1)
		else true
	)
	&& 
	( (*SUD*)
		if j <> m-1 then
		(
			(b.(i).(j+1) <> -1) 
			&& (((b.(i).(j+1) land 0b0111000000000000) lsr 12) = ((t land 0b0000011100000000) lsr 8))
			&& (((b.(i).(j+1) land 0b1000000000000000) lsr 12) <>((t land 0b0000100000000000) lsr 8))
		) || (b.(i).(j+1) = -1) 
		else true
	) 
	&&
	( (*EST*)
		if i <> n-1 then 
		(
			(b.(i+1).(j) <> -1) 
			&& (((b.(i+1).(j) land 0b0000000000000111) lsr 0 ) = ((t land 0b0000000001110000) lsr 4))
			&& (((b.(i+1).(j) land 0b0000000000001000) lsr 0 ) <>((t land 0b0000000010000000) lsr 4))
	 	) || (b.(i+1).(j) = -1)
	 	else true
	)
	&&
	( (*OUEST*)
		if i <> 0 then 
		(	
			(b.(i-1).(j) <> -1) 
			&& (((b.(i-1).(j) land 0b0000000001110000) lsr 4 ) = ((t land 0b0000000000000111) lsr 0))
			&& (((b.(i-1).(j) land 0b0000000010000000) lsr 4 ) <>((t land 0b0000000000001000) lsr 0))
		) || (b.(i-1).(j) = -1)
		else  true
	)


let soltuion_nb = ref 0 

let incr_sol_nb () : unit = 
	soltuion_nb := !soltuion_nb + 1;
	(*au début je pensait compter toutes les solutions
	c'est un peut long.*)
	(if !soltuion_nb mod 1000000000 = 0 then begin
		Printf.printf " found %d billion solutions \n"  (!soltuion_nb/1000000000);
		flush stdout
	end)

let print_board (b : board) : unit = 
	Printf.printf " FOUND A SOLUTION : \n";
	for j = 0 to m-1 do 
		for i = 0 to n-1 do 
			Printf.printf " %x " (b.(i).(j) (*land 0b0111011101110111*) )
		done;
		print_newline()
	done

let rec find_soltution (b : board) (pieces : tuile list) (i : int) (j : int) : unit = 
	if pieces = [] || (j = m) then begin 
		print_board b;
		incr_sol_nb ()
		end 
	else 
	(*print_board b;*)
	let possibles = List.map (fun t -> t,
		[t;
		 t |> rotate_left;
		 t |> rotate_left |> rotate_left;
		 t |> rotate_left |> rotate_left|> rotate_left]
		) pieces in 
	(*List.iter (fun (t,l) -> List.iter (fun t_placed -> 
		Printf.printf " %x - " t_placed
		)l;
		Printf.printf "\n"
	) possibles;*)
	List.iter (fun (t,l) -> 
		List.iter (fun t_placed -> 
			if is_placeable_non_tore b i j t_placed then begin
				b.(i).(j) <- t_placed;
				find_soltution b 
				(List.filter (fun p -> p <> t) pieces)
				((i+1) mod n) 
				(if i+1 = n then (j+1) else j) 
			end else ()
		) l
	) possibles

let _ =
	let b = Array.make_matrix n m (-1) in
	find_soltution b [
	(*BLANC : 01 ROUGE : 11 BLEU : 10*)
	(*dans l'ordre alphabétique*)
	0b1011_1001_1001_0001;
	0b1010_1001_0001_0001;
	0b1010_1011_1011_0011;
	0b0001_0010_1011_1010;
	0b1010_0001_0011_0011;
	0b0010_1010_1010_1010;
	0b0011_1001_1001_0011;
	0b1010_1001_1001_0010;
	0b0010_0011_0011_0010;
	0b1011_1010_1001_0010;
	0b0011_1001_1010_1010;
	0b1011_0011_0011_1011;
	0b0011_1011_1001_1011;
	0b0010_0010_0001_0010;
	0b0010_0010_1011_1010;
	0b0010_1011_1001_1011;
	0b1001_1001_1001_0001;
	0b1001_0010_0001_0011;
	0b1001_0001_1011_1011;
	0b0001_0001_1010_1010;
	0b0011_1011_1010_0010;
	0b1001_0011_1010_1011;
	0b0001_0001_0011_0010;
	0b0001_0011_1001_0010
	]
	0 0;
	Printf.printf "there are about %d solutions total !\n" (!soltuion_nb)

