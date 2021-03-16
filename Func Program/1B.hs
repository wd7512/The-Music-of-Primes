square :: Int -> Int
square x = x*x

pythagoras :: Int -> Int -> Int -> Bool 
pythagoras a b c = square a + square b == square c

factorial :: Int -> Int
factorial n
    | n <= 1    = 1
    | otherwise = n * factorial (n-1)

euclid :: Int -> Int -> Int 
euclid x y
    | x == y    = x
    | x <  y    = euclid x (y-x)
    | otherwise = euclid y (x-y)

power :: Int -> Int -> Int 
power a b
    | b < 0     = undefined 
    | b == 0    = 1
    | otherwise = a * power a (b-1)

range :: Int -> Int -> [Int]
range n m = [n..m]

times :: [Int] -> Int 
times [] = 1
times (x:xs) = x * times xs

fact :: Int -> Int 
fact n = times (range 1 n)