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
  | Lambda   Var Term
  | Apply    Term Term
  deriving show

example :: Term
example = Lambda "a" (Lambda "x" (Apply (Apply (Lambda "y" (Apply (Variable "a") (Variable "c"))) (Variable "x")) (Variable "b")))
