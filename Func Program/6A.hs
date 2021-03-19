{-
data IntTree = Empty | Node Int IntTree IntTree

t :: IntTree
t = Node 4 (Node 2 (Node 1 Empty Empty) (Node 3 Empty Empty)) (Node 5 Empty (Node 6 Empty Empty))

instance Show IntTree where
    show = unlines . aux ' ' ' '
      where
        aux _ _ Empty = []
        aux c d (Node x s t) = 
          [ c:' ':m | m <- aux ' ' '|' s ] ++ 
          ['+':'-':show x] ++ 
          [ d:' ':n | n <- aux '|' ' ' t ]

isEmpty :: IntTree -> Bool
isEmpty Empty = True
isEmpty _     = False
-}

data Tree a = Empty | Node a (Tree a) (Tree a)

instance Show a => Show (Tree a) where
    show = unlines . aux ' ' ' '
      where
        aux _ _ Empty = []
        aux c d (Node x s t) = 
          [ c:' ':m | m <- aux ' ' '|' s ] ++ 
          ['+':'-':show x] ++ 
          [ d:' ':n | n <- aux '|' ' ' t ]

t :: Tree Int
t = Node 4 (Node 2 (Node 1 Empty Empty) (Node 3 Empty Empty)) (Node 5 Empty (Node 6 Empty Empty))

isEmpty :: Tree a -> Bool
isEmpty Empty = True
isEmpty _     = False


member :: Ord a => a -> Tree a -> Bool
member _ Empty               = False
member i (Node x left right) = member i left || member i right || x == i

largest :: Tree a -> a
largest Empty            = error "largest : empty tree"
largest (Node x l Empty) = x
largest (Node x l r)     = largest r

flatten :: Tree a -> [a]
flatten Empty = []
flatten (Node x l r) = flatten l ++ [x] ++ flatten r

sorted :: Ord a => [a] -> Bool
sorted [] = True 
sorted [x]  = True
sorted (x:y:zs) = x < y && sorted (y:zs)

ordered :: Ord a => Tree a -> Bool
ordered = sorted . flatten

deleteLargest :: Tree a -> Tree a
deleteLargest Empty            = error "deleteLargest : empty tree"
deleteLargest (Node x l Empty) = l
deleteLargest (Node x l r)     = (Node x l (deleteLargest r))

delete :: Ord a => a -> Tree a -> Tree a
delete _ Empty = Empty
delete y (Node x l r)
  | y < x     = Node x (delete y l) r
  | y > x     = Node x l (delete y r)
  | isEmpty l = r
  | otherwise = Node (largest l) (deleteLargest l) r

