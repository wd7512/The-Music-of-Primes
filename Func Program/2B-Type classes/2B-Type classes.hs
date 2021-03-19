

ladies    = ["Mary","Kitty","Lydia","Elizabeth","Jane"]
gentlemen = ["Charles","Fitzwilliam","George","William"]
couples   = [("Elizabeth","Fitzwilliam"),("Charlotte","William"),("Lydia","George"),("Jane","Charles")]

------------------------- Exercise 1


ditch :: Int -> [a] -> [a]
ditch = undefined

at :: [a] -> Int -> a
at = undefined


------------------------- Exercise 2

find :: Eq a => a -> [(a,b)] -> b
find = undefined

which :: Eq a => a -> [a] -> Int
which = aux 0
  where
    aux :: Eq a => Int -> a -> [a] -> Int
    aux = undefined

sorted :: Ord a => [a] -> Bool
sorted = undefined

------------------------- Exercise 3

merge :: Ord a => [a] -> [a] -> [a]
merge xs [] = undefined
merge [] ys = undefined
merge (x:xs) (y:ys) = undefined

minus :: Ord a => [a] -> [a] -> [a]
minus = undefined

msort :: Ord a => [a] -> [a]
msort = undefined
