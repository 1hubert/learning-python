import whisper

def main():
    gt_1030_supported_models = ['tiny', 'base', 'small']
    model = whisper.load_model(gt_1030_supported_models[1])
    result = model.transcribe('Finally Reaching Celestia in Genshin Impact by...Walking？.mp3', fp16=False, language='English')
    print(result['text'])


if __name__ == '__main__':
    main()