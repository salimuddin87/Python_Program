import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your Name', help='The person to greet.')
def hello(count, name):
    """
    :param count:
    :param name:
    :return: Greetin to a name provided
    """
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()

# python hello.py --count=3