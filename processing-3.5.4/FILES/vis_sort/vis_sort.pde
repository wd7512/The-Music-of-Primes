
float[] values;
int i;
int j;

void setup() {
  size (240,150);
  frameRate(1000);
  values = new float[width];
  for (int i = 0; i < values.length; i++) {
    values[i] = random(height);
  }
}
  

void swap(float[] arr, int a, int b){
  float temp = arr[a];
  arr[a] = arr[b];
  arr[b] = temp;
}

void draw() {
  background(0);
  for (int i = 0 ; i < width; i++) {
    stroke(255);
    line(i,height,i,height - values[i]);
  }
  float a = values[j];
  float b = values[j+1];
  
  if (a > b) {
    swap (values, j, j+1);
  }
  j = j + 1;
  if (j >= values.length - i - 1){
    j = 0;
    i = i + 1;
  }
}
