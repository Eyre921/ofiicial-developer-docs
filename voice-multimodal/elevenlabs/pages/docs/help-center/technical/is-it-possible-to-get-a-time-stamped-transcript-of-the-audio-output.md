---
title: "Is it possible to get a time stamped transcript of the audio output?"
source: https://elevenlabs.io/docs/help-center/technical/is-it-possible-to-get-a-time-stamped-transcript-of-the-audio-output.md
path: docs/help-center/technical/is-it-possible-to-get-a-time-stamped-transcript-of-the-audio-output
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Is it possible to get a time stamped transcript of the audio output?

While it is not possible to get the transcript of the audio output on the website yet, you can easily get the timestamps of the audio output using our new Timestamps API endpoint for Text-to-speech generation.

You can learn more about it here: [/docs/api-reference/text-to-speech-with-timestamps](/docs/api-reference/text-to-speech-with-timestamps)

The output timestamps would look like:

\{ \
'characters': \['B', 'o', 'r', 'n', ' ', 'a', 'n', 'd', ' ', 'r', 'a', 'i', 's', 'e', 'd', ' ', 'i', 'n', ' ', 't', 'h', 'e', ' ', 'c', 'h', 'a', 'r', 'm', 'i', 'n', 'g', ' ', 's', 'o', 'u', 't', 'h', ',', ' ', 'I', ' ', 'c', 'a', 'n', ' ', 'a', 'd', 'd', ' ', 'a', ' ', 't', 'o', 'u', 'c', 'h', ' ', 'o', 'f', ' ', 's', 'w', 'e', 'e', 't', ' ', 's', 'o', 'u', 't', 'h', 'e', 'r', 'n', ' ', 'h', 'o', 's', 'p', 'i', 't', 'a', 'l', 'i', 't', 'y', ' ', 't', 'o', ' ', 'y', 'o', 'u', 'r', ' ', 'a', 'u', 'd', 'i', 'o', 'b', 'o', 'o', 'k', 's', ' ', 'a', 'n', 'd', ' ', 'p', 'o', 'd', 'c', 'a', 's', 't', 's'], \
'character\_start\_times\_seconds': \[0.0, 0.186, 0.279, 0.348, 0.406, 0.441, 0.476, 0.499, 0.522, 0.58, 0.65, 0.72, 0.778, 0.824, 0.882, 0.906, 0.952, 0.975, 1.01, 1.045, 1.068, 1.091, 1.115, 1.149, 1.196, 1.254, 1.3, 1.358, 1.416, 1.474, 1.498, 1.521, 1.602, 1.66, 1.811, 1.869, 1.927, 1.974, 2.009, 2.043, 2.067, 2.136, 2.183, 2.218, 2.252, 2.287, 2.322, 2.357, 2.392, 2.426, 2.45, 2.508, 2.531, 2.589, 2.635, 2.682, 2.717, 2.763, 2.786, 2.81, 2.879, 2.937, 3.007, 3.065, 3.123, 3.17, 3.239, 3.286, 3.367, 3.402, 3.437, 3.46, 3.483, 3.529, 3.564, 3.599, 3.634, 3.68, 3.75, 3.82, 3.889, 3.971, 4.087, 4.168, 4.214, 4.272, 4.331, 4.389, 4.412, 4.447, 4.528, 4.551, 4.574, 4.609, 4.644, 4.702, 4.748, 4.807, 4.865, 4.923, 5.016, 5.074, 5.12, 5.155, 5.201, 5.248, 5.283, 5.306, 5.329, 5.352, 5.41, 5.457, 5.573, 5.654, 5.735, 5.886, 5.944, 6.06], \
'character\_end\_times\_seconds': \[0.186, 0.279, 0.348, 0.406, 0.441, 0.476, 0.499, 0.522, 0.58, 0.65, 0.72, 0.778, 0.824, 0.882, 0.906, 0.952, 0.975, 1.01, 1.045, 1.068, 1.091, 1.115, 1.149, 1.196, 1.254, 1.3, 1.358, 1.416, 1.474, 1.498, 1.521, 1.602, 1.66, 1.811, 1.869, 1.927, 1.974, 2.009, 2.043, 2.067, 2.136, 2.183, 2.218, 2.252, 2.287, 2.322, 2.357, 2.392, 2.426, 2.45, 2.508, 2.531, 2.589, 2.635, 2.682, 2.717, 2.763, 2.786, 2.81, 2.879, 2.937, 3.007, 3.065, 3.123, 3.17, 3.239, 3.286, 3.367, 3.402, 3.437, 3.46, 3.483, 3.529, 3.564, 3.599, 3.634, 3.68, 3.75, 3.82, 3.889, 3.971, 4.087, 4.168, 4.214, 4.272, 4.331, 4.389, 4.412, 4.447, 4.528, 4.551, 4.574, 4.609, 4.644, 4.702, 4.748, 4.807, 4.865, 4.923, 5.016, 5.074, 5.12, 5.155, 5.201, 5.248, 5.283, 5.306, 5.329, 5.352, 5.41, 5.457, 5.573, 5.654, 5.735, 5.886, 5.944, 6.06, 6.548]\
}
