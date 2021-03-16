doubles :: [Int] -> [Int]
doubles xs = [2*x | x <- xs]

odds :: [Int] -> [Int]
odds xs = [x | x <- xs , odd x]

doubleodds :: [Int] -> [Int]
doubleodds xs = [2*x | x <- xs , odd x]

shorts :: [String] -> [String]
shorts xs = [x | x <- xs, length x <= 5]

squarePositives :: [Int] -> [Int]
squarePositives xs = [x*x | x <- xs , x > 0]

oddLengthSums :: [[Int]] -> [Int]
oddLengthSums xs = [sum x | x <- xs , odd (length x)]

remove :: Eq a => [a] -> a -> [a]
remove xs y = [x | x <- xs , x /= y]

removeAll :: Eq a => [a] -> [a] -> [a]
removeAll xs ys = [x | x <- xs , not (elem x ys)]

everyother :: [a] -> [a]
everyother xs = [x | (x,i) <- zip xs [0..] , even i]

same :: Eq a => [a] -> [a] -> [Int]
same xs ys = [i | (x,y,i) <- zip3 xs ys [0..], x == y]

pairs :: [a] -> [b] -> [(a,b)]
pairs xs ys = [(x,y) | x <- xs , y <- ys]

selfpairs :: [a] -> [(a,a)]
selfpairs xs = [(x,y) | (x,i) <- zip xs [0..], (y,j) <- zip xs [0..] , j >= i]

pyts :: Int -> [(Int,Int,Int)]
pyts n = [(a,b,c) | c <- [1..n], a <- [1..c], b <- [1..a] , (a*a + b*b) == c*c]