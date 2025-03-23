from diffusers import StableDiffusionPipeline


model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id)

prompt = "A BMW Boat with futuristic design"
image = pipe(prompt).images[0]


image.save("BMW_Boat.png")


from diffusers import StableDiffusionPipeline


model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id)


prompt = "A BMW fighter tank to robust engineering"
image = pipe(prompt).images[0]


image.save("BMW_Tank.png")
