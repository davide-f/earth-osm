from earth_osm.eo import get_osm_data


def test_building():
    get_osm_data(
        region_list=["benin"],
        primary_name="building",
        feature_list=None,
        update=False,
        mp=True,
        out_format=["csv", "geojson"],
        out_aggregate=False,
    )

    
if __name__ == '__main__':
    test_building()