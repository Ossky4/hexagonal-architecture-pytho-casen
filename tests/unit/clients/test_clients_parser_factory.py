import pytest

from src.clients.application.clients_parser import CSVClientsParser, JSONClientsParser, ParserFactory
from src.clients.application.dto import ExportFormat


@pytest.mark.parametrize(
    ("output_format", "expected_parser_class"),
    [
        (ExportFormat.CSV, CSVClientsParser),
        (ExportFormat.JSON, JSONClientsParser),
    ],
)
def test_parser_factory_builds_parser_from_export_format(
    output_format: ExportFormat, expected_parser_class: type[CSVClientsParser | JSONClientsParser]
) -> None:
    parser = ParserFactory.build(output_format)

    assert isinstance(parser, expected_parser_class)
