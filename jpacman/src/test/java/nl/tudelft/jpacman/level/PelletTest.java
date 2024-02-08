package nl.tudelft.jpacman.level;

import nl.tudelft.jpacman.npc.Ghost;
import nl.tudelft.jpacman.npc.ghost.GhostFactory;
import nl.tudelft.jpacman.points.DefaultPointCalculator;
import nl.tudelft.jpacman.sprite.PacManSprites;
import nl.tudelft.jpacman.sprite.Sprite;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

public class PelletTest {
    private static final PacManSprites SPRITE_STORE = new PacManSprites();
    private final DefaultPointCalculator ptCalc = new DefaultPointCalculator();
    private final GhostFactory gFactory = new GhostFactory(SPRITE_STORE);
    private final LevelFactory Factory = new LevelFactory(SPRITE_STORE, gFactory, ptCalc);
    private final Pellet ThePellet = Factory.createPellet();

    @Test
    void testPelletSprite(){
        //create the pellet
        Sprite pelletSprite = SPRITE_STORE.getPelletSprite();
        int pointVal = 10;
        Pellet testPellet = new Pellet(pointVal, pelletSprite);

        //test that the sprite is correctly being set
        assertThat(testPellet.getSprite()).isNotEqualTo(null);

        //test that the point values are correctly being set
        assertThat(testPellet.getValue()).isNotEqualTo(0);
    }
}
