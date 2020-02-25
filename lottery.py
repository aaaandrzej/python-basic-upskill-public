import click
import os
from participant import extract_participants_from_csv, extract_participants_from_json
from prize import extract_prizes_from_scheme
from winner import draw_winners, write_winners_to_json, print_winners


def default_scheme_file(directory):
    for item in os.listdir(directory):
        if os.path.isfile(directory + item):
            return directory + item
    #
    # return (directory + item for item in os.listdir(directory) if os.path.isfile(directory + item))  # chciałem tak ale nie działa :)


# default_scheme = ("data/lottery_templates/" + os.listdir("data/lottery_templates")[0])  # zamienione na funkcję powyżej
default_scheme = default_scheme_file("data/lottery_templates/")


@click.command()
@click.argument("file_input")
@click.option('--file_extension', type=click.Choice(['json', 'csv']), default="json", help='Extension of the filename with participants, default is json')  # TODO użyc choices czy jakoś tak - tylko 2 opcje - DONE
@click.option('--scheme', default=default_scheme,  # TODO powinien pobierać pierwszy alfabetycznie plik z folderu - DONE
              help='Filename with lottery scheme, default is data/lottery_templates/item_giveaway.json')
@click.option('--file_output', default="data/result.json", help='Output json file, default is data/result.json')
def main(file_input, file_extension, scheme, file_output):
    click.echo("Witamy w loterii")

    if file_extension == "json":
        file_content = extract_participants_from_json(file_input)
    elif file_extension == "csv":
        file_content = extract_participants_from_csv(file_input)

    prizes = extract_prizes_from_scheme(scheme)

    winners_with_prizes = draw_winners(file_content, prizes)

    write_winners_to_json(winners_with_prizes, file_output)
    print_winners(winners_with_prizes)

    summary = f"(wylosowano z {file_input} z użyciem {scheme} i zapisano do {file_output})"
    print(summary)


if __name__ == "__main__":

    main()  # file_input argument required, e.g.: "python lottery.py participants1.json"
    # print(default_scheme_file("data/lottery_templates/"))
