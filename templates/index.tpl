<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible"
              content="IE=edge, chrome=1" />
        <title>Python Job Openings In The Philippines - Python PH</title>
    </head>
    <body>
        <a href="/add">Add Company &raquo;</a>
        <table summary="List of available Python companies that have job openings in the Philippines."
               border="1">
            <caption>Python Job Openings In The Philippines</caption>
            <thead>
                <tr>
                    <th id="name">Name:</th>
                    <th id="description">Description:</th>
                    <th id="uri">URI:</th>
                    <th id="Source">Source:</th>
                </tr>
            </thead>
            <tfoot>
                <tr>
                    <td colspan="4">&copy; PythonPH 2014</td>
                </tr>
            </tfoot>
            <tbody>
                % for company in companies:
                <tr>
                    <td headers="name">{{company['name']}}</td>
                    <td headers="description">{{company['description']}}</td>
                    <td headers="uri">
                        <a href="{{company['uri']}}">{{company['uri']}}</a>
                    </td>
                    <td headers="source">{{company['source']}}</td>
                </tr>
                % end
            </tbody>
        </table>
    </body>
</html>
