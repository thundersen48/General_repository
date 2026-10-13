for i := 1 to length(S) do begin
	  substring := true;
	  for j := 1 to length(T) do
	    if (S[i] <> T[j]) then
	      substring := false;
	  if substring then
	    //добавляем в список вхождений
	end;