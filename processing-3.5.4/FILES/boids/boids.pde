void setup(){
  size (800,800);
  frameRate(60);
  
  pos = new PVector[boidnum];
  dir = new float[boidnum];
  for (int i = 0; i < boidnum; i++){
    pos[i] = new PVector(width/2,height/2);
    dir[i] = random(0,TWO_PI);
  }
}

void draw(){
  background(255);
  for (int i = 0; i < boidnum; i++){
    drawBoid(dir[i],pos[i].x,pos[i].y);
    
    PVector d = new PVector(boidspeed*cos(dir[i]),boidspeed*sin(dir[i]));
    
    if (pos[i].x < boidrange){ //if off to the left too much
      
      
    }
    
    dir[i] = dir[i] % TWO_PI;
    
    pos[i].add(d);
  }
  
}

int boidsize = 5;
PVector [] pos;
float[] dir;


int boidrange = 50;
int boidnum = 10;
int boidspeed = 1;


void drawBoid(float dir, float x, float y){
  float x1 = x + 2 * boidsize * cos(dir);
  float y1 = y + 2 * boidsize * sin(dir);
  float x2 = x + boidsize * cos(dir + TWO_PI / 3);
  float y2 = y + boidsize * sin(dir + TWO_PI / 3);
  float x3 = x + boidsize * cos(dir + 2 * TWO_PI / 3);
  float y3 = y + boidsize * sin(dir + 2 * TWO_PI / 3);
  triangle(x1,y1,x2,y2,x3,y3);
}
