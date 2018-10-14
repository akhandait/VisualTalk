# VisualTalk

### This is a trained image captioning model in [torch](http://torch.ch/) for [InOut 2018](https://hackinout.co/).

**main.py** is a python script which calls **eval.lua** with the required arguments.

When executed on the CPU, each image takes ~**1.4** seconds to get captioned.

The eval script will create an `vis.json` file inside the `vis` folder, which can then be visualized with the provided HTML interface:

```
$ cd vis
$ python3 -m SimpleHTTPServer
```

Thanks to [Andrej Karpathy](https://github.com/karpathy) for the [pretrained weights](http://cs.stanford.edu/people/karpathy/neuraltalk2/checkpoint_v1.zip).

