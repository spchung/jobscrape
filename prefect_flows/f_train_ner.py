'''
This flow will train new or improve existing NER models
'''

@task
def define_task(
    n_iter: int,
    model: str,
    output_dir: str
): pass