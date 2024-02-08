package nl.tudelft.jpacman.level;

import nl.tudelft.jpacman.npc.Ghost;
import nl.tudelft.jpacman.npc.ghost.GhostFactory;
import nl.tudelft.jpacman.points.DefaultPointCalculator;
import nl.tudelft.jpacman.points.PointCalculator;
import nl.tudelft.jpacman.sprite.AnimatedSprite;
import nl.tudelft.jpacman.sprite.PacManSprites;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

/**
 * New Test Case example
 * @author John Businge
 */
public class PlayerTest {
    /**
     * I prefer to save the instances for this test in particular
     * because it is really a pain to instantiate Player, and I
     * will want to test other methods of Player in here.
     */
    private static final PacManSprites SPRITE_STORE = new PacManSprites();
    private final PlayerFactory Factory = new PlayerFactory(SPRITE_STORE);
    private final Player ThePlayer = Factory.createPacMan();


    //create a collision object
    private  final DefaultPointCalculator ptCalc = new DefaultPointCalculator();
    private final PlayerCollisions collision = new PlayerCollisions(ptCalc);

    //create a ghost object
    //use Blinky as the type
    private final GhostFactory gFactory = new GhostFactory(SPRITE_STORE);
    private final Ghost TheGhost = gFactory.createBlinky();


    @Test
    void testAlive(){
        assertThat(ThePlayer.isAlive()).isEqualTo(true);
    }

    @Test
    void testAddPoints(){
        //test to see if the addPoints function is correctly adding points
        int pointValue = 1;
        ThePlayer.addPoints(pointValue);
        assertThat(ThePlayer.getScore()).isNotEqualTo(0);
    }

    @Test
    void testPlayerVersusGhost(){
        collision.playerVersusGhost(ThePlayer, TheGhost);

        //test to see that the player is correctly dead
        assertThat(ThePlayer.isAlive()).isEqualTo(false);

        //test to see if the killer is correctly being set
        assertThat(ThePlayer.getKiller()).isEqualTo(TheGhost);
    }
}
