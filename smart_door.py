import cv2
import face_recognition
import serial


s = serial.Serial("COM1", 9600)
#json_file = open("config.json")
#gmail_cfg = json.load(json_file)

#print(gmail_cfg)

# Load a sample image with known faces


known_image = face_recognition.load_image_file("Ayoub.jpg")

# Encode the known face(s)
known_face_encoding = face_recognition.face_encodings(known_image)[0]

# Capture video from your webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Read the current frame
    ret, frame = video_capture.read()

    # Convert the frame from BGR to RGB
    rgb_frame = frame[:, :, ::-1]
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Find all faces in the frame
    face_locations = face_recognition.face_locations(rgb_frame)
    #if len(face_locations) > 0:
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding in face_encodings:
        # Compare the detected face(s) with the known face(s)
        matches = face_recognition.compare_faces([known_face_encoding], face_encoding)
        name = "Unknown"
        #s.write(str.encode('0'))
       
        if matches[0]:
            name = "Known"
            data = 1
        s.write("1".encode())
        
        if not matches[0]:
            name = "UnKnown"
            data = 0
        s.write("0".encode())
        # Draw a rectangle around the face
        top, right, bottom, left = face_locations[0]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Display the name
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)
    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the windows
video_capture.release()
cv2.destroyAllWindows()
 
 