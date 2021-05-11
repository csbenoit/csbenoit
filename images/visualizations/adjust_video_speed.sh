ffmpeg -i HD163296_12CO_channelmap_RichardTeague.mp4 -filter_complex "[0:v]trim=0:4.7,setpts=PTS-STARTPTS[v1]; [0:v]trim=4.7:8,setpts=3.8*(PTS-STARTPTS)[v2]; [0:v]trim=8:10,setpts=PTS-STARTPTS[v3]; [0:v]trim=10:10.6,setpts=5*(PTS-STARTPTS)[v4]; [0:v]trim=10.6,setpts=PTS-STARTPTS[v5]; [v1][v2][v3][v4][v5]concat=n=5:v=1" HD163296_12CO_channelmap_RichardTeague_slowdown.mp4

ffmpeg -i MWC480_12CO_channelmap_RichardTeague.mp4 -filter_complex "[0:v]trim=0:5.3,setpts=PTS-STARTPTS[v1]; [0:v]trim=5.3:8.3,setpts=3.3*(PTS-STARTPTS)[v2]; [0:v]trim=8.3,setpts=PTS-STARTPTS[v3]; [v1][v2][v3]concat=n=3:v=1" MWC480_12CO_channelmap_RichardTeague_slowdown.mp4
