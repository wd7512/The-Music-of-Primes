import random
a100=a99=a98=a97=a96=a95=a94=a93=a92=a91=a90=a89=a88=a87=a86=a85=a84=a83=a82=a81=a80=a79=a78=a77=a76=a75=a74=a73=a72=a71=a70=a69=a68=a67=a66=a65=a64=a63=a62=a61=a60=a59=a58=a57=a56=a55=a54=a53=a52=a51=a50=a49=a48=a47=a46=a45=a44=a43=a42=a41=a40=a39=a38=a37=a36=a35=a34=a33=a32=a31=a30=a29=a28=a27=a26=a25=a24=a23=a22=a21=a20=a19=a18=a17=a16=a15=a14=a13=a12=a11=a10=a9=a8=a7=a6=a5=a4=a3=a2=a1='_'
board = (a100+a99+a98+a97+a96+a95+a94+a93+a92+a91+'\n'+a90+a89+a88+a87+a86+a85+a84+a83+a82+a81+'\n'+a80+a79+a78+a77+a76+a75+a74+a73+a72+a71+'\n'+a70+a69+a68+a67+a66+a65+a64+a63+a62+a61+'\n'+a60+a59+a58+a57+a56+a55+a54+a53+a52+a51+'\n'+a50+a49+a48+a47+a46+a45+a44+a43+a42+a41+'\n'+a40+a39+a38+a37+a36+a35+a34+a33+a32+a31+'\n'+a30+a29+a28+a27+a26+a25+a24+a23+a22+a21+'\n'+a20+a19+a18+a17+a16+a15+a14+a13+a12+a11+'\n'+a10+a9+a8+a7+a6+a5+a4+a3+a2+a1)
print(board)
blist=[a100, a99, a98, a97, a96, a95, a94, a93, a92, a91, a90, a89, a88, a87, a86, a85, a84, a83, a82, a81, a80, a79, a78, a77, a76, a75, a74, a73, a72, a71, a70, a69, a68, a67, a66, a65, a64, a63, a62, a61, a60, a59, a58, a57, a56, a55, a54, a53, a52, a51, a50, a49, a48, a47, a46, a45, a44, a43, a42, a41, a40, a39, a38, a37, a36, a35, a34, a33, a32, a31, a30, a29, a28, a27, a26, a25, a24, a23, a22, a21, a20, a19, a18, a17, a16, a15, a14, a13, a12, a11, a10, a9, a8, a7, a6, a5, a4, a3, a2, a1]
num=random.choice(blist)
print(num)
print([i for i,x in enumerate(blist) if x == num])
