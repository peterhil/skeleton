class Listing
    constructor: (container) ->
        @data = []
        @elem = $(container).text('Loading...')
        @template = '''<div class="item">
    <p><a href="{{ url }}">{{ url }}</a></p>
</div>'''
        @url = app.apiUrl() + '/api/v1/items'
        app.ajax(@url)
            .done (data) =>
                @elem.text 'Parsing data...'
                @show data

    show: (data) =>
        @elem.text ''
        if not data? or data.length == 0
            @elem.text('No items yet.')
            @data = []
            return false

        # Ugly hack for now to get rid of DustJS
        out = _.join(_.map(
            data.items,
            (item) =>
                _.template(@template)({url: item.url})), "\n")

        @elem.html(out)


if $('.listing').length > 0
    app.items = new Listing($('.listing'))
