#include <stdio.h>

#define CHANNELS 30
#define THRESHOLD 150.0

void process_signal(float buffer[CHANNELS]) {
    for(int i = 0; i < CHANNELS; i++) {
        if(buffer[i] > THRESHOLD) {
            printf("Artifact detected on Channel %d\n", i);
        }
    }
}

int main() {
    float sample_data[CHANNELS] = {0.0};
    process_signal(sample_data);
    return 0;
}
