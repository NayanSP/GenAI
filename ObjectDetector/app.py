import gradio as gr
from PIL import Image, ImageDraw, ImageFont
import scipy.io.wavfile as wavfile
from transformers import pipelines

narrator = pipelines('text-to-speech',
                     model = "kakao-enterprise/vits-ljs")

obj_detect = pipelines('object-detection',
                       model = "facebook/detr-resnet-50")

def generate_Audio(text):
    narrated_text = narrator(text)
    wavfile.write('op.wav', 
                  rate=narrated_text['sampling_rate'],
                  data=narrated_text['audio'][0])
    return 'op.wav'

def read_obj(detect_obj):
    obj_cnt = {}

    for detect in detect_obj:
        label = detect['label']
        if label in obj_cnt:
            obj_cnt[label]+=1
        else:
            obj_cnt[label] = 1

    resp = 'This pircture contains '
    labels = list(obj_cnt.keys())
    for i, label in enumerate(labels):
        resp += f" {obj_cnt[label]} {label}"
        if obj_cnt[label] > 1:
            resp += 's'
        if i< len(labels) -2:
            resp += ','
        elif i == len(labels) - 2:
            resp += ' and'
    
    resp += "."

    return resp

def draw_bounding_boxes(image, detections, font_path=None, font_size=20):
    """
    Draws bounding boxes on the given image based on the detections.
    :param image: PIL.Image object
    :param detections: List of detection results, where each result is a dictionary containing
                       'score', 'label', and 'box' keys. 'box' itself is a dictionary with 'xmin',
                       'ymin', 'xmax', 'ymax'.
    :param font_path: Path to the TrueType font file to use for text.
    :param font_size: Size of the font to use for text.
    :return: PIL.Image object with bounding boxes drawn.
    """
    # Make a copy of the image to draw on
    draw_image = image.copy()
    draw = ImageDraw.Draw(draw_image)

    # Load custom font or default font if path not provided
    if font_path:
        font = ImageFont.truetype(font_path, font_size)
    else:
        # When font_path is not provided, load default font but it's size is fixed
        font = ImageFont.load_default()
        # Increase font size workaround by using a TTF font file, if needed, can download and specify the path

    for detection in detections:
        box = detection['box']
        xmin = box['xmin']
        ymin = box['ymin']
        xmax = box['xmax']
        ymax = box['ymax']

        # Draw the bounding box
        draw.rectangle([(xmin, ymin), (xmax, ymax)], outline="red", width=3)

        # Optionally, you can also draw the label and score
        label = detection['label']
        score = detection['score']
        text = f"{label} {score:.2f}"

        # Draw text with background rectangle for visibility
        if font_path:  # Use the custom font with increased size
            text_size = draw.textbbox((xmin, ymin), text, font=font)
        else:
            # Calculate text size using the default font
            text_size = draw.textbbox((xmin, ymin), text)

        draw.rectangle([(text_size[0], text_size[1]), (text_size[2], text_size[3])], fill="red")
        draw.text((xmin, ymin), text, fill="white", font=font)

    return draw_image


def detect_object(image):
    raw_image = image
    output = object_detector(raw_image)
    processed_image = draw_bounding_boxes(raw_image, output)
    natural_text = read_objects(output)
    processed_audio = generate_audio(natural_text)
    return processed_image, processed_audio


demo = gr.Interface(fn=detect_object,
                    inputs=[gr.Image(label="Select Image",type="pil")],
                    outputs=[gr.Image(label="Processed Image", type="pil"), gr.Audio(label="Generated Audio")],
                    title="@GenAILearniverse Project 7: Object Detector with Audio",
                    description="THIS APPLICATION WILL BE USED TO HIGHLIGHT OBJECTS AND GIVES AUDIO DESCRIPTION FOR THE PROVIDED INPUT IMAGE.")
demo.launch()

# print(output)
