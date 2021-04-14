void setup() {
  size (1000,1000);
  frameRate(60);
  xpos = new float[noTri];
  ypos = new float[noTri];
  dir = new float[noTri];
  for (int i = 0; i < noTri; i++){
    xpos[i] = width/2;
    ypos[i] = height/2;
    dir[i] = random(TWO_PI);
  }
}

float trisize = 5;
int noTri = 2000;
float [] xpos;
float [] ypos;
float [] dir;
float speed = 10;


void tri(float ang, float x, float y){ // ang goes from 0 to 2*pi
  float x1 = x + 2 * trisize * cos(ang);
  float y1 = y + 2 * trisize * sin(ang);
  float x2 = x + trisize * cos(ang + TWO_PI / 3);
  float y2 = y + trisize * sin(ang + TWO_PI / 3);
  float x3 = x + trisize * cos(ang + 2 * TWO_PI / 3);
  float y3 = y + trisize * sin(ang + 2 * TWO_PI / 3);
  triangle(x1,y1,x2,y2,x3,y3);
}



void draw() {
  background(255);
  for (int i = 0; i < noTri; i++){
    tri(dir[i],xpos[i],ypos[i]);

    float dx = speed * cos(dir[i]);
    float dy = speed * sin(dir[i]);
    

    
    if (xpos[i] + dx < trisize*speed) {dir[i] = PI - dir[i];dx = speed * cos(dir[i]);}
    if (xpos[i] + dx > width - trisize*speed) {dir[i] = PI - dir[i];dx = speed * cos(dir[i]);}
    if (ypos[i] + dy < trisize*speed) {dir[i] = - dir[i];dy = speed * sin(dir[i]);}
    if (ypos[i] + dy > height - trisize*speed) {dir[i] =- dir[i];dy = speed * sin(dir[i]);}

    
    xpos[i] = xpos[i] + dx;
    ypos[i] = ypos[i] + dy;
  }
}
