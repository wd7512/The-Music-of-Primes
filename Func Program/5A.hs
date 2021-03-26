data IntTree = Empty | Node Int IntTree IntTree

instance Show IntTree where
    show = unlines . aux ' ' ' '
      where
        aux _ _ Empty = []
        aux c d (Node x s t) = 
          [ c:' ':m | m <- aux ' ' '|' s ] ++ 
          ['+':'-':show x] ++ 
          [ d:' ':n | n <- aux '|' ' ' t ]

t :: IntTree
t = Node 4 (Node 2 (Node 1 Empty Empty) (Node 3 Empty Empty)) (Node 5 Empty (Node 6 Empty Empty))


isEmpty :: IntTree -> Bool
isEmpty Empty = True 
isEmpty _     = False

rootValue :: IntTree -> Int 
rootValue Empty = 0
rootValue (Node x left right) = x

height :: IntTree -> Int 
height Empty = 0
height (Node x left right) = max (height left) (height right) + 1

member :: Int -> IntTree -> Bool 
member _ Empty = False 
member y (Node x left right) = y == x || member y left || member y right

type Var = String

data Term =
    Variable Var
  | Lambda   Var  Term
  | Apply    Term Term

instance Show Term where
  show = pretty

example :: Term
example = Lambda "a" (Lambda "x" (Apply (Apply (Lambda "y" (Apply (Variable "a") (Variable "c"))) (Variable "x")) (Variable "b")))

pretty :: Term -> String
pretty = f 0
    where
      f i (Variable x) = x
      f i (Lambda x m) = if i /= 0 then "(" ++ s ++ ")" else s where s = "\\" ++ x ++ ". " ++ f 0 m 
      f i (Apply  n m) = if i == 2 then "(" ++ s ++ ")" else s where s = f 1 n ++ " " ++ f 2 m

n1 :: Term
n1 = Lambda "x" (Variable "x")

n2 :: Term
n2 = Lambda "x" (Apply (Lambda "y" (Variable "x")) (Variable "z"))

n3 :: Term
n3 = Apply (Lambda "x" (Lambda "y" (Apply (Variable "x") (Variable "y")))) n1

used :: Term -> [Var]
used (Variable x) = [x]
used (Lambda x y) = merge [x] (used y)
used (Apply x y)  = merge (used x) (used y)

free :: Term -> [Var]
free (Variable x) = [x]
free (Lambda x y) = minus (free y) [x]
free (Apply x y)  = merge (free x) (free y)
-------

merge :: Ord a => [a] -> [a] -> [a]
merge xs [] = xs
merge [] ys = ys
merge (x:xs) (y:ys)
    | x == y    = x : merge xs ys
    | x <= y    = x : merge xs (y:ys)
    | otherwise = y : merge (x:xs) ys

minus :: Ord a => [a] -> [a] -> [a]
minus xs [] = xs
minus [] ys = []
minus (x:xs) (y:ys)
    | x <  y    = x : minus    xs (y:ys)
    | x == y    =     minus    xs    ys
    | otherwise =     minus (x:xs)   ys
