# Helping-Eye

###Inspiration
Our team has members from Odisha, a coastal state in India affected by cyclones every year. We also hail from a country (India) where we experience a continuous array of disasters distributed across the topography (Flood in some parts, earthquakes in others) and the effect of such calamities is devastating. Considering cyclones, the Super Cyclone (1999) and Fani (2019) were the most notable ones where airspeed went up to 160 mph after landfall. The cyclone’s eye passing through the place is quite terrifying but even more catastrophic is the aftermath. People can’t find their relatives, their pets, cattle, their loved ones. Disaster Relief Team searches frantically in every part of the city requiring a lot of time, resources and manpower but still, there are places where a relief team can’t reach. That’s where we want to help, covering those inaccessible areas using an eye which is similar to a human rescuer’s eye.

###What it does and how I built it
We plan to boost-up this search and relief process by deploying Artificial Intelligence. We plan to use a drone to capture live video footage of certain areas affected by the cyclone and relay them back to the center along with the GPS coordinates. The center would be having a Neural Network architecture running on a powerful machine that would detect the frames wherever there are survivors and flag the GPS coordinate of the drone. We have used a Faster R-CNN architecture that detects objects trained on the MSCOCO dataset. Hence, it can detect people and animals with great accuracy. The performance of the algorithm can be significantly improved by the underlying processing speed of the center which has been implemented in the algorithm.

###Challenges I ran into
Real-time detection with a less powerful machine is very hard to achieve in the real world. We had to use the GPU of our machine to run the "Detection". We had planned on deploying this method to the drones directly but it has been pushed to future hackathons.

###Accomplishments that I'm proud of
A client (drone) is sending the video feed to the server-side (Data-Center) in low resolution given the bandwidth constraints. This video is then analyzed by our algorithm which uses a Faster R-CNN (high accuracy and fast detection) and then detecting survivors in the aftermath of a natural disaster. After this, we have devised a way to flag off whenever survivors are detected in the video feed and then notifying the response team with the GPS coordinates of the flagged area.

###What I learned
Using state-of-the-art NN image detection architecture. Working with PyTorch, deploying such algorithms in real-life.

###What's next for Helping Eye
This can be further extended to run a pre-trained low resource (less accuracy, kind of like the first pass) Neural net architecture on the drone itself and flagging the Relief teams faster, and then sending the feed to Center as the second pass. The Data-Center block can be used as a second pass to assure we have high accuracy in the entire system. The algorithm can be fine-tuned to run on low resources as a Raspberry Pi module attached to a drone. Drones can talk to each other and notify other drones about hot areas, such that those drones can automatically scan such areas which will increase the field of view.

###Built With
Python PyTorch
