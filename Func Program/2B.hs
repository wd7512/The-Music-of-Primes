ladies    = ["Mary","Kitty","Lydia","Elizabeth","Jane"]
gentlemen = ["Charles","Fitzwilliam","George","William"]
couples   = [("Elizabeth","Fitzwilliam"),("Charlotte","William"),("Lydia","George"),("Jane","Charles")]

ditch :: Int -> [a] -> [a]
ditch 0 xs = xs
ditch n (x:xs) = ditch (n-1) xs 

at :: [a] -> Int -> a
at (x:_)  0 = x
at (_:xs) n = at xs (n-1)

