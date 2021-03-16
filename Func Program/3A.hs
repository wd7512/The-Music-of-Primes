double :: Int -> Int 
double x = 2*x

doubles :: [Int] -> [Int]
doubles = map double

odds :: [Int] -> [Int]
odds = filter odd

doubleodds :: [Int] -> [Int]
doubleodds = map double . odds

shorts :: [String ] -> [String ]
shorts = filter f
    where
        f x = length x <= 5

squarePositives :: [Int] -> [Int]
squarePositives = map f . filter g
    where
        f x = x * x
        g x = x > 0

oddLengthSums :: [[Int]] -> [Int]
oddLengthSums = map sum . filter g
    where 
        g x = odd (length x)