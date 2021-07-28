### About: 
```bash
The SoundBoat is a Discord Bot, that can join your channel via the command !sb play [name of sound].
He than plays the sound you chose and leaves the channel.
A list of sounds can be viewed with the command !sb help

The SQLite database can be edited with simple SQL commands: 
    To add a sound: INSERT INTO sounds (name, fileName) VALUES ('Test', 'test.mp3');
    To remove a sound: DELETE FROM sounds WHERE name = 'Test'
    To edit a sound: UPDATE sounds SET name = 'Test2' WHERE name = 'Test'
    To list all current sounds: SELECT * from sounds

Obviously the .mp3 file of every sound in the database has to placed inside the 'SoundBoat sounds' file
```