void setup() {
  size (800,500);
  frameRate(60);
  xpos = new float[noTri];
  ypos = new float[noTri];
  dir = new float[noTri];
  for (int i = 0; i < noTri; i++){
    xpos[i] = random(width);
    ypos[i] = random(height);
    dir[i] = random(TWO_PI);
  }
}

float trisize = 5;
int noTri = 100;
float [] xpos;
float [] ypos;
float [] dir;
float speed = 3;
float vision = 100;
float turnSpeed = 0.01;


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
    dir[i] = dir[i];
    xpos[i] = xpos[i] + speed * cos(dir[i]);
    ypos[i] = ypos[i] + speed * sin(dir[i]);
    

    for (int j = 0; j < noTri; j++){
      if (i != j){

        float dist = (abs(xpos[i] - xpos[j]) + abs(ypos[i] - ypos[j]));
        if (dist < vision) {
          float between = atan((ypos[j]-ypos[i])/(xpos[j]-xpos[i]));
          float diff = between - dir[i];
          if (diff <  -PI) {dir[i] = dir[i] - turnSpeed * vision / dist;} // go away anti
          //if (diff > -PI && diff < 0) {dir[i] = dir[i] + 0.1 * turnSpeed * dist / vision;} // go towards clock
          //if (diff > 0 && diff < PI) {dir[i] = dir[i] - 0.1 * turnSpeed * dist / vision;} // go towards anti
          if (diff > PI) {dir[i] = dir[i] + turnSpeed * vision / dist;} // go away clock
          
        }
      }
    }
    if (xpos[i] < 0) {xpos[i] = width;}
    if (xpos[i] > width) {xpos[i] = 0;}
    if (ypos[i] < 0) {ypos[i] = height;}
    if (ypos[i] > height) {ypos[i] = 0;}
  }
}
