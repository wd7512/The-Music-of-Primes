ladies    = ["Mary","Kitty","Lydia","Elizabeth","Jane"]
gentlemen = ["Charles","Fitzwilliam","George","William"]
couples   = [("Elizabeth","Fitzwilliam"),("Charlotte","William"),("Lydia","George"),("Jane","Charles")]

ditch :: Int -> [a] -> [a]
ditch 0 xs = xs
ditch n (x:xs) = ditch (n-1) xs 

at :: [a] -> Int -> a
at (x:_)  0 = x
at (_:xs) n = at xs (n-1)

find :: Eq a => a -> [(a,b)] -> b
find _ [] = error "item not found"
find x ((y,z):zs)
    | x == y    = z
    | otherwise = find x zs 

which :: Eq a => a -> [a] -> Int
which = aux 0
    where
        aux :: Eq a => Int -> a -> [a] -> Int
        aux _ x [] = error "item not found"
        aux i x (y:ys)
            | x == y    = i
            | otherwise = aux (i+1) x ys



member :: Eq a => [a] -> a -> Bool
member [] _     = False
member (x:xs) y
    | x == y    = True 
    | otherwise = member xs y

remove :: Eq a => [a] -> a -> [a]
remove [] _     = []
remove (x:xs) y
    | x == y    = xs
    | otherwise = x : remove xs y

before :: Ord a => [a] -> [a] -> Bool 
before _ [] = False
before [] _ = True
before (x:xs) (y:ys)
    | x < y     = True 
    | x == y    = before xs ys
    | otherwise = False


sorted :: Ord a => [a] -> Bool 
sorted [] = True 
sorted [x]  = True
sorted (x:y:zs) = x < y && sorted (y:zs)

merge :: Ord a => [a] -> [a] -> [a]
merge xs [] = xs
merge [] ys = ys
merge (x:xs) (y:ys)
    | x < y     = x : merge xs (y:ys)
    | x > y     = y : merge (x:xs) ys
    | otherwise = x : merge xs ys

minus :: Ord a => [a] -> [a] -> [a]
minus xs [] = xs
minus [] ys = []
minus xs (y:ys)
    | member xs y = minus (remove xs y) ys
    | otherwise   = minus xs ys

msort :: Ord a => [a] -> [a]
msort [] = []
msort [x] = [x]
msort xs = merge (msort (take n xs)) (msort (drop n xs))
    where
        n = div (length xs) 2
