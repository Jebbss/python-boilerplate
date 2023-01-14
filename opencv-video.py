import os
import cv2


def to_video(paths_to_frames, fps, width, height, output_path):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(os.path.join(output_path, 'output.avi'), fourcc, fps, (width, height))

    for path in paths_to_frames:
        frame = cv2.imread(path)
        out.write(frame)

    out.release()
    cv2.destroyAllWindows()