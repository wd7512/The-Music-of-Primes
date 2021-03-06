
--------------------------------------------
--                                        --
-- CM20256/CM50262 Functional Programming --
--                                        --
--         Coursework 2020/2021           --
--                                        --
--------------------------------------------


------------------------- Auxiliary functions

{-# OPTIONS_GHC -Wno-deferred-type-errors #-}
find :: (Show a,Eq a) => a -> [(a,b)] -> b
find x [] = error ("find: " ++ show x ++ " not found")
find x ((y,z):zs)
  | x == y    = z
  | otherwise = find x zs


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


------------------------- Lambda-terms

type Var = String

data Term =
    Variable Var
  | Lambda   Var  Term
  | Apply    Term Term
  deriving Eq


instance Show Term where
  show = f 0
    where
      f i (Variable x) = x
      f i (Lambda x m) = if i /= 0 then "(" ++ s ++ ")" else s where s = "\\" ++ x ++ ". " ++ f 0 m 
      f i (Apply  n m) = if i == 2 then "(" ++ s ++ ")" else s where s = f 1 n ++ " " ++ f 2 m

free :: Term -> [Var]
free (Variable x) = [x]
free (Lambda x n) = free n `minus` [x]
free (Apply  n m) = free n `merge` free m


------------------------- Types

infixr 5 :->

type Atom = String
data Type = At Atom | Type :-> Type
  deriving Eq

instance Show Type where
  show (At a)       = a
  show (At a :-> s) = a ++ " -> " ++ show s
  show    (t :-> s) = "(" ++ show t ++ ") -> " ++ show s


atoms :: [Atom]
atoms = map (:[]) ['a'..'z'] ++ [ a : show i | i <- [1..], a <- ['a'..'z'] ]

t1 :: Type
t1 = At "a" :-> At "b"

t2 :: Type
t2 = (At "c" :-> At "d") :-> At "e"

t3 :: Type
t3 = At "a" :-> At "c" :-> At "c"


------------------------- Assignment 1

t4 :: Atom -> Type
t4 x = At x :-> At "b"

occurs :: Atom -> Type -> Bool
occurs x (At a)    = a == x 
occurs x (a :-> b) = occurs x a || occurs x b


findAtoms :: Type -> [Atom]
findAtoms (At a) = [a]
findAtoms (a :-> b) = merge (findAtoms a) (findAtoms b) {-merge merges alphabetically -}


------------------------- Type substitution

type Sub = (Atom,Type)

s1 :: Sub
s1 = ("a", At "e")

s2 :: Sub
s2 = ("e", At "b" :-> At "c")

s3 :: Sub
s3 = ("c", At "a" :-> At "a")


------------------------- Assignment 2

sub :: Sub -> Type -> Type
sub (x, m) (At a)
  | x == a    = m
  | otherwise = At a
sub (x, m) (a :-> b)
  | (At x) == a = m :-> (sub (x, m) b)
  | (At x) == b = (sub (x, m) a) :-> m
  | otherwise   = (sub (x, m) a) :-> (sub (x, m) b)


subs :: [Sub] -> Type -> Type
subs [] m     = m
subs [x] m    = sub x m
subs (x:xs) m = sub x (subs xs m)

------------------------- Unification

type Upair = (Type,Type)
type State = ([Sub],[Upair])

u1 :: Upair
u1 = (t1,At "c")

u2 :: Upair
u2 = (At "a" :-> At "a",At "a" :-> At "c")

u3 :: Upair
u3 = (t1,t2)

u4 :: Upair
u4 = (t2,t3)

st1 :: State
st1 = ([],[u1,u2])


------------------------- Assignment 3

sub_u :: Sub -> [Upair] -> [Upair]
sub_u x [(m,n)] = [(sub x m, sub x n)]
sub_u x (m:ms) = (sub_u x [m]) ++ (sub_u x ms)

step :: State -> State
step (s,[]) = (s,[])
step (s, (At a, At b):xs)
  | a == b    = (s,xs)
  | otherwise = ((a,At b):s, [(sub (a,At b) p, sub (a,At b) q )| (p,q) <- xs])
step (s, (At a, m):xs)
  | occurs a m = error ("Exception: STEP: Atom " ++ show a ++ " Occurs in " ++ show m)
  | otherwise  = ((a,m):s, [(sub (a,m) p, sub (a,m) q )| (p,q) <- xs])
step (s, (m, At a):xs)
  | occurs a m = error ("Exception: STEP: Atom " ++ show a ++ " Occurs in " ++ show m)
  | otherwise  = ((a,m):s, [(sub (a,m) p, sub (a,m) q )| (p,q) <- xs])
step (s, (a :-> m,b :-> n):xs) = (s, (a, b):(m ,n):xs)


unify :: [Upair] -> [Sub]
unify x
  | u == []   = s
  | otherwise = unify' (s,u)
    where
      (s,u) = step ([],x)

      unify' :: State -> [Sub]
      unify' (s,u)
        | u == []   = s
        | otherwise = unify' (step (s,u))

------------------------- Assignment 4

type Context   = [(Var,Type)]
type Judgement = (Context,Term,Type)

data Derivation = Axiom Judgement | Abstraction Judgement Derivation | Application Judgement Derivation Derivation


n1 :: Term
n1 = Apply (Lambda "x" (Variable "x")) (Variable "y")


d1 :: Derivation
d1 = Application ([("y",At "a")], n1 , At "a") (
       Abstraction ([("y",At "a")],Lambda "x" (Variable "x"),At "a" :-> At "a") (
         Axiom ([("x",At "a"),("y",At "a")],Variable "x",At "a")
     ) ) (
       Axiom ([("y",At "a")], Variable "y", At "a")
     )

d2 :: Derivation
d2 = Application ([("y",At "b")],Apply (Lambda "x" (Apply (Variable "x") (Variable "y"))) (Lambda "z" (Variable "z")),At "a") (
       Abstraction ([("y",At "b")],Lambda "x" (Apply (Variable "x") (Variable "y")),At "c") (
         Application ([("x",At "d"),("y",At "b")],Apply (Variable "x") (Variable "y"),At "e") (
           Axiom ([("x",At "d"),("y",At "b")],Variable "x",At "f")
         ) (
           Axiom ([("x",At "d"),("y",At "b")],Variable "y",At "g")
     ) ) ) (
       Abstraction ([("y",At "b")],Lambda "z" (Variable "z"),At "h") (
         Axiom ([("z",At "i"),("y",At "b")],Variable "z",At "j")
     ) )


conclusion :: Derivation -> Judgement
conclusion (Axiom x) = x
conclusion (Abstraction x y) = x
conclusion (Application x y z) = x


subs_ctx :: [Sub] -> Context -> Context
subs_ctx s c 
  | c == []   = []
  | otherwise = (x,subs s m):(subs_ctx s xs)
    where
      (x,m):xs = c


subs_jdg :: [Sub] -> Judgement -> Judgement
subs_jdg s (c,x,t) = (subs_ctx s c, x, subs s t)

subs_der :: [Sub] -> Derivation -> Derivation
subs_der s (Axiom x) = Axiom (subs_jdg s x)
subs_der s (Abstraction x y) = Abstraction (subs_jdg s x) (subs_der s y)
subs_der s (Application x y z) = Application (subs_jdg s x) (subs_der s y) (subs_der s z)

------------------------- Typesetting derivations


instance Show Derivation where
  show d = unlines (reverse strs)
    where
      (_,_,_,strs) = showD d

      showC :: Context -> String
      showC [] = []
      showC [(x,t)]    = x ++ ": " ++ show t
      showC ((x,t):cx) = x ++ ": " ++ show t  ++ " , " ++ showC cx

      showJ :: Judgement -> String
      showJ ([],n,t) =              "|- " ++ show n ++ " : " ++ show t
      showJ (cx,n,t) = showC cx ++ " |- " ++ show n ++ " : " ++ show t

      showL :: Int -> Int -> Int -> String
      showL l m r = replicate l ' ' ++ replicate m '-' ++ replicate r ' '

      showD :: Derivation -> (Int,Int,Int,[String])
      showD (Axiom j) = (0,k,0,[s,showL 0 k 0]) where s = showJ j; k = length s
      showD (Abstraction j d)   = addrule (showJ j) (showD d)
      showD (Application j d e) = addrule (showJ j) (sidebyside (showD d) (showD e))

      addrule :: String -> (Int,Int,Int,[String]) -> (Int,Int,Int,[String])
      addrule x (l,m,r,xs)
        | k <= m     = (ll,k,rr, (replicate ll ' ' ++ x ++ replicate rr ' ') : showL  l m r  : xs)
        | k <= l+m+r = (ll,k,rr, (replicate ll ' ' ++ x ++ replicate rr ' ') : showL ll k rr : xs)
        | otherwise  = (0,k,0, x : replicate k '-' : [ replicate (-ll) ' ' ++ y ++ replicate (-rr) ' ' | y <- xs])
        where
          k = length x
          i = div (m - k) 2
          ll = l+i
          rr = r+m-k-i

      extend :: Int -> [String] -> [String]
      extend i strs = strs ++ repeat (replicate i ' ')

      sidebyside :: (Int,Int,Int,[String]) -> (Int,Int,Int,[String]) -> (Int,Int,Int,[String])
      sidebyside (l1,m1,r1,d1) (l2,m2,r2,d2)
        | length d1 > length d2 = ( l1 , m1+r1+2+l2+m2 , r2 , [ x ++ "  " ++ y | (x,y) <- zip d1 (extend (l2+m2+r2) d2)])
        | otherwise             = ( l1 , m1+r1+2+l2+m2 , r2 , [ x ++ "  " ++ y | (x,y) <- zip (extend (l1+m1+r1) d1) d2])



------------------------- Assignment 5

contextOccurs :: Var -> Context -> Bool
contextOccurs x y = aux x [a | (a,_) <- y]
  where
    aux :: Var -> [Var] -> Bool
    aux x []     = False
    aux x (y:ys) = x == y || aux x ys

derive0 :: Term -> Derivation
derive0 x = aux ([(a,At "") | a <- free x],x,At "")
  where
    aux :: Judgement -> Derivation
    aux (c,Variable x,t)
      | contextOccurs x c = Axiom (c, Variable x, At "")
      | otherwise         = Axiom ([(x,At "")] ++ c, Variable x, At "")

    aux (c,Lambda x y,t)
      | contextOccurs x c = Abstraction (c,Lambda x y,At "") (aux ([(x,At "")] ++ [(a,b) | (a,b) <- c, a /= x],y, At ""))
      | otherwise         = Abstraction (c,Lambda x y, At "") (aux ([(x,At"")] ++ c,y, At ""))

    aux (c,Apply x y,t) = Application (c,Apply x y,At "") (aux (c,x, At "")) (aux (c,y, At ""))


derive1 :: Term -> Derivation
derive1 x = aux (drop (1 + length (free x)) atoms) ([(a,At b) | (a,b) <- zip (free x) (tail atoms)],x, At (head atoms))
  where
    aux :: [Atom] -> Judgement -> Derivation
    aux ats (c,Variable x,t)
      | contextOccurs x c = Axiom (c, Variable x, t)
      | otherwise         = Axiom ([(x,At (head (tail ats)))] ++ c, Variable x, t)

    aux ats (c,Lambda x y,t)
      | contextOccurs x c = Abstraction (c,Lambda x y, t) (aux (drop 2 ats) ([(x,At (head ats))] ++ [(a,b) | (a,b) <- c, a /= x],y, At (head (tail ats))))
      | otherwise         = Abstraction (c,Lambda x y, t) (aux (drop 2 ats) ([(x,At (head ats))] ++ c,y, At (head (tail ats))))

    aux ats (c,Apply x y,t) = Application 
                              (c,Apply x y, t) 
                              (aux [a | (a,i) <- zip (drop 2 ats) [0..], even i] (c,x, At (head ats))) 
                              (aux [a | (a,i) <- zip (drop 2 ats) [0..], odd i] (c,y,At (head (tail ats))))


upairs :: Derivation -> [Upair]
upairs (Axiom (c,Variable x,t)) = [(t,find x c)]

upairs (Abstraction (c1,Lambda x1 y1,t1) p) = [(t1, (find x1 c2) :-> t2)] ++ upairs p
  where
    (c2,x2,t2) = conclusion p

upairs (Application (c1,Apply x1 y1,t1) p q) = [(t2,t3 :-> t1)] ++ upairs p ++ upairs q
  where
    (c2,x2,t2) = conclusion p
    (c3,x3,t3) = conclusion q


derive :: Term -> Derivation
derive x = subs_der (unify (upairs (derive1 x))) (derive1 x)

test1 = Lambda "x" (Lambda "y" (Lambda "z" (Apply(Apply(Variable "x")(Variable "z"))(Apply(Variable "y")(Variable "z")))))
test2 = Lambda "x" (Lambda "x" (Variable "x"))
test3 = Lambda "x" (Lambda "y" (Lambda "z" (Apply(Apply(Variable "x")(Variable "z"))(Apply(Variable "y")(Variable"z")))))
test4 = Lambda "x" (Lambda "x" (Lambda "y" (Lambda "y" (Apply (Variable "x") (Variable "y")))))    