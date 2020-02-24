import click
from participant import extract_participants_from_csv, extract_participants_from_json
from prize import extract_prizes_from_scheme
from winner import draw_winners, write_winners_to_json, print_winners


@click.command()
@click.argument("file_input")
@click.option('--file_extension', default="json",
              help='Extension of the filename with participants, default is json')
@click.option('--scheme', default="data/lottery_templates/item_giveaway.json",
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

'''
# scripts for testing only - commented by default
    file_input="data/participants2.json"
    file_extension="json"
    scheme="data/lottery_templates/item_giveaway.json"
    file_output="data/result.json"

    if file_extension == "json":
        file_content = extract_participants_from_json(file_input)
    elif file_extension == "csv":
        file_content = extract_participants_from_csv(file_input)

    prizes = extract_prizes_from_scheme(scheme)

    winners_with_prizes = draw_winners(file_content, prizes)

    # write_winners_to_json(winners_with_prizes, file_output)
    #
    # print_winners(winners_with_prizes)
    #
    # summary = f"(wylosowano z {file_input} z użyciem {scheme} i zapisano do {file_output})"
    #
    # print(summary)

    print(winners_with_prizes)
'''
